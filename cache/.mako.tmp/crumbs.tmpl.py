# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1438424261.002727
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/crumbs.tmpl'
_template_uri = u'crumbs.tmpl'
_source_encoding = 'utf-8'
_exports = ['bar']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 19
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,crumbs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        if crumbs:
            # SOURCE LINE 5
            __M_writer(u'<nav class="breadcrumbs">\n<ul class="breadcrumb">\n')
            # SOURCE LINE 7
            for link, text in crumbs:
                # SOURCE LINE 8
                if text != index_file:
                    # SOURCE LINE 9
                    if link == '#':
                        # SOURCE LINE 10
                        __M_writer(u'                <li>')
                        __M_writer(unicode(text.rsplit('.html', 1)[0]))
                        __M_writer(u'</li>\n')
                        # SOURCE LINE 11
                    else:
                        # SOURCE LINE 12
                        __M_writer(u'                <li><a href="')
                        __M_writer(unicode(link))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a></li>\n')
            # SOURCE LINE 16
            __M_writer(u'</ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


