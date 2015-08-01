# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1438424259.673114
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/bootstrap3/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_headstart', 'html_navigation_links', 'html_stylesheets', 'html_translations', 'html_feedlinks']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'notes', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        # SOURCE LINE 93
        __M_writer(u'\n\n\n')
        # SOURCE LINE 127
        __M_writer(u'\n\n')
        # SOURCE LINE 150
        __M_writer(u'\n\n')
        # SOURCE LINE 173
        __M_writer(u'\n\n')
        # SOURCE LINE 181
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        colorbox_locales = _import_ns.get('colorbox_locales', context.get('colorbox_locales', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 68
        __M_writer(u'\n')
        # SOURCE LINE 69
        if use_bundles:
            # SOURCE LINE 70
            if use_cdn:
                # SOURCE LINE 71
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
                # SOURCE LINE 74
            else:
                # SOURCE LINE 75
                __M_writer(u'            <script src="/assets/js/all-nocdn.js"></script>\n')
            # SOURCE LINE 77
        else:
            # SOURCE LINE 78
            if use_cdn:
                # SOURCE LINE 79
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>\n')
                # SOURCE LINE 81
            else:
                # SOURCE LINE 82
                __M_writer(u'            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            # SOURCE LINE 87
            __M_writer(u'        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        # SOURCE LINE 89
        if colorbox_locales[lang]:
            # SOURCE LINE 90
            __M_writer(u'        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(unicode(colorbox_locales[lang]))
            __M_writer(u'.js"></script>\n')
        # SOURCE LINE 92
        __M_writer(u'    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        mathjax_config = _import_ns.get('mathjax_config', context.get('mathjax_config', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        striphtml = _import_ns.get('striphtml', context.get('striphtml', UNDEFINED))
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        use_open_graph = _import_ns.get('use_open_graph', context.get('use_open_graph', UNDEFINED))
        def html_feedlinks():
            return render_html_feedlinks(context)
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        twitter_card = _import_ns.get('twitter_card', context.get('twitter_card', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<!DOCTYPE html>\n<html\n')
        # SOURCE LINE 8
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            # SOURCE LINE 9
            __M_writer(u"prefix='")
            # SOURCE LINE 10
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                # SOURCE LINE 11
                __M_writer(u'og: http://ogp.me/ns# ')
            # SOURCE LINE 13
            if use_open_graph:
                # SOURCE LINE 14
                __M_writer(u'article: http://ogp.me/ns/article# ')
            # SOURCE LINE 16
            if comment_system == 'facebook':
                # SOURCE LINE 17
                __M_writer(u'fb: http://ogp.me/ns/fb# ')
            # SOURCE LINE 19
            __M_writer(u"'")
        # SOURCE LINE 22
        if is_rtl:
            # SOURCE LINE 23
            __M_writer(u'dir="rtl" ')
        # SOURCE LINE 26
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n    <head>\n    <meta charset="utf-8">\n')
        # SOURCE LINE 29
        if description:
            # SOURCE LINE 30
            __M_writer(u'    <meta name="description" content="')
            __M_writer(unicode(description))
            __M_writer(u'">\n')
        # SOURCE LINE 32
        __M_writer(u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <title>')
        # SOURCE LINE 33
        __M_writer(striphtml(unicode(title)))
        __M_writer(u' | ')
        __M_writer(striphtml(unicode(blog_title)))
        __M_writer(u'</title>\n\n    ')
        # SOURCE LINE 35
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 36
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n')
        # SOURCE LINE 37
        if permalink:
            # SOURCE LINE 38
            __M_writer(u'      <link rel="canonical" href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if favicons:
            # SOURCE LINE 42
            for name, file, size in favicons:
                # SOURCE LINE 43
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        # SOURCE LINE 46
        __M_writer(u'\n')
        # SOURCE LINE 47
        if comment_system == 'facebook':
            # SOURCE LINE 48
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 51
        if prevlink:
            # SOURCE LINE 52
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(prevlink))
            __M_writer(u'" type="text/html">\n')
        # SOURCE LINE 54
        if nextlink:
            # SOURCE LINE 55
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(nextlink))
            __M_writer(u'" type="text/html">\n')
        # SOURCE LINE 57
        __M_writer(u'\n    ')
        # SOURCE LINE 58
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        # SOURCE LINE 59
        if use_cdn:
            # SOURCE LINE 60
            __M_writer(u'        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
            # SOURCE LINE 61
        else:
            # SOURCE LINE 62
            __M_writer(u'        <!--[if lt IE 9]><script src="')
            __M_writer(unicode(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer(u'"></script><![endif]-->\n')
        # SOURCE LINE 64
        __M_writer(u'\n    ')
        # SOURCE LINE 65
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 129
        __M_writer(u'\n')
        # SOURCE LINE 130
        for url, text in navigation_links[lang]:
            # SOURCE LINE 131
            if isinstance(url, tuple):
                # SOURCE LINE 132
                __M_writer(u'            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(unicode(text))
                __M_writer(u' <b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                # SOURCE LINE 134
                for suburl, text in url:
                    # SOURCE LINE 135
                    if rel_link(permalink, suburl) == "#":
                        # SOURCE LINE 136
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(permalink))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u' <span class="sr-only">')
                        __M_writer(unicode(messages("(active)", lang)))
                        __M_writer(u'</span></a>\n')
                        # SOURCE LINE 137
                    else:
                        # SOURCE LINE 138
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                # SOURCE LINE 141
                __M_writer(u'            </ul>\n')
                # SOURCE LINE 142
            else:
                # SOURCE LINE 143
                if rel_link(permalink, url) == "#":
                    # SOURCE LINE 144
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(permalink))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u' <span class="sr-only">')
                    __M_writer(unicode(messages("(active)", lang)))
                    __M_writer(u'</span></a>\n')
                    # SOURCE LINE 145
                else:
                    # SOURCE LINE 146
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        notes = _mako_get_namespace(context, 'notes')
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'\n')
        # SOURCE LINE 97
        if use_bundles:
            # SOURCE LINE 98
            if use_cdn:
                # SOURCE LINE 99
                __M_writer(u'            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
                # SOURCE LINE 101
            else:
                # SOURCE LINE 102
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 104
        else:
            # SOURCE LINE 105
            if use_cdn:
                # SOURCE LINE 106
                __M_writer(u'            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">\n')
                # SOURCE LINE 107
            else:
                # SOURCE LINE 108
                __M_writer(u'            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 110
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 114
            if has_custom_css:
                # SOURCE LINE 115
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        # SOURCE LINE 118
        if needs_ipython_css:
            # SOURCE LINE 119
            __M_writer(u'        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        # SOURCE LINE 122
        if annotations and post and not post.meta('noannotations'):
            # SOURCE LINE 123
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
            # SOURCE LINE 124
        elif not annotations and post and post.meta('annotations'):
            # SOURCE LINE 125
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 175
        __M_writer(u'\n')
        # SOURCE LINE 176
        for langname in sorted(translations):
            # SOURCE LINE 177
            if langname != lang:
                # SOURCE LINE 178
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(abs_link(_link("root", None, langname))))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        rss_link = _import_ns.get('rss_link', context.get('rss_link', UNDEFINED))
        generate_rss = _import_ns.get('generate_rss', context.get('generate_rss', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        generate_atom = _import_ns.get('generate_atom', context.get('generate_atom', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 152
        __M_writer(u'\n')
        # SOURCE LINE 153
        if rss_link:
            # SOURCE LINE 154
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
            # SOURCE LINE 155
        elif generate_rss:
            # SOURCE LINE 156
            if len(translations) > 1:
                # SOURCE LINE 157
                for language in sorted(translations):
                    # SOURCE LINE 158
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
                # SOURCE LINE 160
            else:
                # SOURCE LINE 161
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        # SOURCE LINE 164
        if generate_atom:
            # SOURCE LINE 165
            if len(translations) > 1:
                # SOURCE LINE 166
                for language in sorted(translations):
                    # SOURCE LINE 167
                    __M_writer(u'                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('index_atom', None, language)))
                    __M_writer(u'">\n')
                # SOURCE LINE 169
            else:
                # SOURCE LINE 170
                __M_writer(u'            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(unicode(_link('index_atom', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


