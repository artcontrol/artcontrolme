# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1438423377.389289
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/bootstrap3/templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'pheader', context._clean_inheritance_tokens(), templateuri=u'post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pheader')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pheader = _mako_get_namespace(context, 'pheader')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 28
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 51
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 59
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pheader = _mako_get_namespace(context, 'pheader')
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n<article class="post-')
        # SOURCE LINE 31
        __M_writer(unicode(post.meta('type')))
        __M_writer(u' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        # SOURCE LINE 32
        __M_writer(unicode(pheader.html_post_header()))
        __M_writer(u'\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
        # SOURCE LINE 34
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    </div>\n    <aside class="postpromonav">\n    <nav>\n    ')
        # SOURCE LINE 38
        __M_writer(unicode(helper.html_tags(post)))
        __M_writer(u'\n    ')
        # SOURCE LINE 39
        __M_writer(unicode(helper.html_pager(post)))
        __M_writer(u'\n    </nav>\n    </aside>\n')
        # SOURCE LINE 42
        if not post.meta('nocomments') and site_has_comments:
            # SOURCE LINE 43
            __M_writer(u'        <section class="comments hidden-print">\n        <h2>')
            # SOURCE LINE 44
            __M_writer(unicode(messages("Comments")))
            __M_writer(u'</h2>\n        ')
            # SOURCE LINE 45
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer(u'\n        </section>\n')
        # SOURCE LINE 48
        __M_writer(u'    ')
        __M_writer(unicode(helper.mathjax_script(post)))
        __M_writer(u'\n</article>\n')
        # SOURCE LINE 50
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        # SOURCE LINE 9
        if post.meta('keywords'):
            # SOURCE LINE 10
            __M_writer(u'    <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'">\n')
        # SOURCE LINE 12
        if post.description():
            # SOURCE LINE 13
            __M_writer(u'    <meta name="description" itemprop="description" content="')
            __M_writer(unicode(post.description()))
            __M_writer(u'">\n')
        # SOURCE LINE 15
        __M_writer(u'    <meta name="author" content="')
        __M_writer(unicode(post.author()))
        __M_writer(u'">\n')
        # SOURCE LINE 16
        if post.prev_post:
            # SOURCE LINE 17
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(post.prev_post.permalink()))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(unicode(post.prev_post.title())))
            __M_writer(u'" type="text/html">\n')
        # SOURCE LINE 19
        if post.next_post:
            # SOURCE LINE 20
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(post.next_post.permalink()))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(unicode(post.next_post.title())))
            __M_writer(u'" type="text/html">\n')
        # SOURCE LINE 22
        if post.is_draft:
            # SOURCE LINE 23
            __M_writer(u'        <meta name="robots" content="noindex">\n')
        # SOURCE LINE 25
        __M_writer(u'    ')
        __M_writer(unicode(helper.open_graph_metadata(post)))
        __M_writer(u'\n    ')
        # SOURCE LINE 26
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n    ')
        # SOURCE LINE 27
        __M_writer(unicode(helper.meta_translations(post)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n')
        # SOURCE LINE 54
        if show_sourcelink:
            # SOURCE LINE 55
            __M_writer(u'    <li>\n    <a href="')
            # SOURCE LINE 56
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


