def popnext(stream, token):
	if stream[0:len(token)] == list(token):
		del stream[0:len(token)]
		return True
	return False

def parse_binary(stream, operator, nextfn):
	es = [nextfn(stream)]
	while popnext(stream, operator):
		es.append(nextfn(stream))
	return '(' + ' {} '.format(operator).join(es) + ')' if len(es) > 1 else es[0]

def parse_ors(stream):
	return parse_binary(stream, 'or', parse_ands)

def parse_ands(stream):
	return parse_binary(stream, 'and', parse_unary)

def parse_unary(stream):
	if popnext(stream, 'not'):
		return '(not {})'.format(parse_unary(stream))
	return parse_primary(stream)

def parse_primary(stream):
	if popnext(stream, '('):
		e = parse_ors(stream)
		popnext(stream, ')')
		return e
	return stream.pop(0)

def evaluate(expression):
	return parse_ors(list(expression.replace(' ', '')))[1:-1]