def transform_errors(errs):
    res = ''
    for key in errs:
        for err in errs[key]:
            res += str(err)
    return {'error': res}
