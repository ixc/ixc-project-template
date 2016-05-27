from itertools import chain, combinations

from django.test import RequestFactory


# See: https://docs.python.org/2/library/itertools.html#recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def get_compress_offline_context():
    # These will be included in every context.
    global_context = {
        'base_change_form_template': 'admin/change_form.html',
        'change_form_template': 'admin/change_form.html',
        'request': RequestFactory().get('/'),
    }
    # Every combination of these will generate a new context. Be careful not to
    # include too many!
    context_powerset = (
        ('base_change_form_template', 'admin/fluent_pages/page/base_change_form.html'),
    )
    for context_vars in powerset(context_powerset):
        context = {}
        context.update(global_context)
        context.update(context_vars)
        yield context
