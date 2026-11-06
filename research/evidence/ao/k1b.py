exec(open('knockout.py').read().split('run("baseline")')[0])
def k_both():
    r1=k_sanitize(); o=ve._terms_with_assignments
    ve._terms_with_assignments=lambda term_result,spec:[(t,list(t.attributes)) for t in term_result.terms if t.attributes]
    def r(): r1(); ve._terms_with_assignments=o
    return r
run("K1b_no_sanitizer_and_no_second_guard",k_both)
