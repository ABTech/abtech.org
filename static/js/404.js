/**
 * @fileoverview Provies a nice light effect for the 404 page.
 *
 * @author Oscar Bezi (oscar@bezi.io)
 */

//==============================================================================
// Global constants.
//==============================================================================
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

/**
 * Curried function that lowpasses a given input with a given low-pass gain.
 *
 * @param {Number} gain - The low-pass gain, must be between 0 and 1.
 * @param {Number} prev - The previous value.
 * @param {Number} new - The new value that's being low-passed in.
 *
 * @returns {Number} The new value low-passed into the previous one.
 */
function lowpass(gain) {
  return function (big, small) {
    return big * (1 - gain) + small * gain;
  };
}

/**
 * Used to lowpass the mouse input slightly, in order to get a smoother
 * response to the mouse snapping in to the screen after leaving it.
 */
var INPUT_LOWPASS_CONST = 1.0;
var input_lowpass = lowpass(INPUT_LOWPASS_CONST);

/**
 * Used to slowly drift the light focus to the center of the screen after a
 * certain timeout.
 */
var CENTER_LOWPASS_CONST = 0.01;
var center_lowpass = lowpass(CENTER_LOWPASS_CONST);

// The timeout before we start to drift to the center after a mouse move.
var TIMEOUT_LENGTH = 1000;

/**
 * Assorted constants for rendering the lights.
 */
// The barrel length.
var LIGHT_HEIGHT = 70;

// The barrel width.
var LIGHT_WIDTH = 40;

// The height of the light base.
var BASE_OFFSET = LIGHT_HEIGHT / 8;

// The beam spread angle.
var BEAM_ANGLE = 12; // Degrees

// The width of the lens bezel (the amount of space between the outside of the
// barrel and the light output).
var LENS_BEZEL_WIDTH = 10;

// Coefficient to convert DEGREES_TO_RADS.
var DEGREES_TO_RADS = Math.PI / 180;

// Some colors.
var BARREL_COLOR = 'white';
var BASE_COLOR = '#252525';

//==============================================================================
// Application default state.
//==============================================================================

var state = {
  'has_moved': false,
  'light_focus': {
    'x': window.innerWidth / 2,
    'y': window.innerHeight / 2,
  },
  'lights': [],
};

//==============================================================================
// Global functions.
//==============================================================================

var previous_timeout = null;

/**
 * Callback for the mousemove event, updates the mouse position within the
 * canvas and sets a callback that re-enables drifting after a certain timeout.
 *
 * @param {Object} mouse_event - The mouse movement event.
 */
function update_position(event) {
  var bounds = canvas.getBoundingClientRect();

  var light_focus = {
    'x': input_lowpass(state.light_focus.x, event.clientX - bounds.left),
    'y': input_lowpass(state.light_focus.y, event.clientY - bounds.top),
  };

  state = Object.assign({}, state, {
    'light_focus': light_focus,
    'has_moved': true,
  });

  if (previous_timeout !== null) {
    clearTimeout(previous_timeout);
  }

  previous_timeout = setTimeout(function() {
    state = Object.assign({}, state, {
      'has_moved': false,
    });
    previous_timeout = null;
  }, TIMEOUT_LENGTH);
}

/**
 * Called whenever the screen resizes (and on page load).
 */
function on_resize() {
  var width = window.innerWidth;
  var height = window.innerHeight;

  var lights = [];
  for (var i = 50; i < width / 2; i += 500) {
    lights.push({
      'x': i,
      'y': 0,
    });

    lights.push({
      'x': i,
      'y': height,
      'flipped': true,
    });

    lights.push({
      'x': width - i,
      'y': 0,
    });

    lights.push({
      'x': width - i,
      'y': height,
      'flipped': true,
    });
  }

  state = Object.assign({}, state, {
    'lights': lights,
  });
}

/**
 * Iterates the state forward whenever a frame render occurs.
 *
 * @param {Object} prev_state - The previous state.
 * @returns {Object} The new state.
 */
function update_state(prev_state) {
  var target_x = window.innerWidth / 2;
  var target_y = window.innerHeight / 2;

  var prev_x = prev_state.light_focus.x;
  var prev_y = prev_state.light_focus.y;

  var has_moved = prev_state.has_moved;

  var light_focus = {
    'x': has_moved ? prev_x : center_lowpass(prev_x, target_x),
    'y': has_moved ? prev_y : center_lowpass(prev_y, target_y),
  };

  return Object.assign({}, prev_state, {
    'light_focus': light_focus,
  });
}

function render_beam(light, light_focus) {
  var light_pivot_x = light.x;
  var light_pivot_y = light.y;
  light_pivot_y += BASE_OFFSET * (light.flipped ? -2 : 2);

  var focus_offset_x = light_focus.x - light_pivot_x;
  var focus_offset_y = light_focus.y - light_pivot_y;
  var angle = Math.atan2(focus_offset_y, focus_offset_x);

  var length = Math.sqrt(canvas.width * canvas.width + canvas.height * canvas.height);

  context.save();

  context.translate(light_pivot_x, light_pivot_y);
  context.rotate(angle - Math.PI / 2);

  // Draw beam
  context.globalAlpha = 0.1;
  context.fillStyle = 'rgba(255, 255, 255, 0.1)';
  context.beginPath();

  var start_x = -LIGHT_WIDTH / 2 + LENS_BEZEL_WIDTH;
  var end_x = start_x - length * Math.sin(BEAM_ANGLE * DEGREES_TO_RADS);

  context.moveTo(start_x, LIGHT_HEIGHT - BASE_OFFSET);
  context.lineTo(end_x, length);
  context.lineTo(-end_x, length);
  context.lineTo(-start_x, LIGHT_HEIGHT - BASE_OFFSET);
  context.closePath();

  context.save();
  context.globalCompositeOperation = 'destination-out';
  context.fillStyle = 'rgb(255, 255, 255, 0.9)';
  context.fill();
  context.restore();

  context.fillStyle = 'rgb(255, 255, 255, 0.9)';
  context.fill();

  context.restore();
}

/**
 * Renders a fixture at the given position.
 *
 * @TODO: Has a lot of nasty render code that should get cleaned.
 * @TODO: The beams should likely get rendered in their own stage, then the
 * actual fixtures.
 *
 * @param {Object} light - The light to render, as found in the global state.
 * @param {Object} light_focus - The light focus destination
 */
function render_light(light, light_focus) {
  var light_pivot_x = light.x;
  var light_pivot_y = light.y;
  light_pivot_y += BASE_OFFSET * (light.flipped ? -2 : 2);

  var focus_offset_x = light_focus.x - light_pivot_x;
  var focus_offset_y = light_focus.y - light_pivot_y;
  var angle = Math.atan2(focus_offset_y, focus_offset_x);

  context.save();
  context.translate(light_pivot_x, light_pivot_y);
  context.rotate(angle - Math.PI / 2);

  // Draw barrel
  context.fillStyle = BARREL_COLOR;
  context.fillRect(-LIGHT_WIDTH / 2, -BASE_OFFSET, LIGHT_WIDTH, LIGHT_HEIGHT);
  context.restore();

  // Draw base
  context.fillStyle = BASE_COLOR;
  context.fillRect(
    light_pivot_x - LIGHT_WIDTH / 4, light_pivot_y, LIGHT_WIDTH / 2, light.flipped ? BASE_OFFSET * 3 : -1 * BASE_OFFSET * 3);
  context.beginPath();
  context.arc(light_pivot_x, light_pivot_y, LIGHT_WIDTH / 4, 0, 2 * Math.PI, false);
  context.fill();
}

function render(to_render) {
  var width = window.innerWidth;
  var height = window.innerHeight;

  canvas.width = width;
  canvas.height = height;

  context.fillStyle = 'rgba(0, 0, 0, 0.9)';
  context.fillRect(0, 0, width, height);

  // Render all the light beams.
  to_render.lights.forEach(function (light) {
    render_beam(light, to_render.light_focus);
  });

  // Render all the fixtures.
  to_render.lights.forEach(function (light) {
    render_light(light, to_render.light_focus);
  });
}

function update() {
  state = update_state(state);
  render(state);

  window.requestAnimationFrame(update);
}

canvas.addEventListener('mousemove', update_position, false);

window.addEventListener('resize', on_resize, false);
on_resize();

window.requestAnimationFrame(update);
