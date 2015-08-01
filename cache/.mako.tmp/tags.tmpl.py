# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1438424260.649634
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/bootstrap3/templates/tags.tmpl'
_template_uri = u'tags.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        cat_items = context.get('cat_items', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        title = context.get('title', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 38
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cat_items = context.get('cat_items', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        title = context.get('title', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<h1>')
        # SOURCE LINE 5
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n')
        # SOURCE LINE 6
        if cat_items:
            # SOURCE LINE 7
            if items:
                # SOURCE LINE 8
                __M_writer(u'        <h2>')
                __M_writer(unicode(messages("Categories")))
                __M_writer(u'</h2>\n')
            # SOURCE LINE 10
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                # SOURCE LINE 11
                for i in range(indent_change_before):
                    # SOURCE LINE 12
                    __M_writer(u'            <ul class="unstyled">\n')
                # SOURCE LINE 14
                __M_writer(u'        <li><a class="reference badge" href="')
                __M_writer(unicode(link))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
                # SOURCE LINE 15
                if indent_change_after <= 0:
                    # SOURCE LINE 16
                    __M_writer(u'            </li>\n')
                # SOURCE LINE 18
                for i in range(-indent_change_after):
                    # SOURCE LINE 19
                    __M_writer(u'            </ul>\n')
                    # SOURCE LINE 20
                    if i + 1 < len(indent_levels):
                        # SOURCE LINE 21
                        __M_writer(u'                </li>\n')
            # SOURCE LINE 25
            if items:
                # SOURCE LINE 26
                __M_writer(u'        <h2>')
                __M_writer(unicode(messages("Tags")))
                __M_writer(u'</h2>\n')
        # SOURCE LINE 29
        if items:
            # SOURCE LINE 30
            __M_writer(u'    <ul class="list-inline">\n')
            # SOURCE LINE 31
            for text, link in items:
                # SOURCE LINE 32
                if text not in hidden_tags:
                    # SOURCE LINE 33
                    __M_writer(u'            <li><a class="reference badge" href="')
                    __M_writer(unicode(link))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
            # SOURCE LINE 36
            __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


