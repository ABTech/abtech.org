STYLE_SRCS = less-src/styles-top.less
STYLE_OUTPUT_PATH = static/css
STYLE_OUTPUT_FILENAME = styles.css

all: styles

cleanstyles:
	rm -rf $(STYLE_OUTPUT_PATH)

styles: cleanstyles
	mkdir -p $(STYLE_OUTPUT_PATH)
	lessc $(STYLE_SRCS) > $(STYLE_OUTPUT_PATH)/$(STYLE_OUTPUT_FILENAME)

rundev: all
	./manage.py runserver

clean: cleanstyles

