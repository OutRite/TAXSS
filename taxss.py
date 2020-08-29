# https://github.com/OutRite/TAXSS
# dont actually use this pls

def sanitize_xss(unfiltered):
	unfiltered = unfiltered.replace('<', '&lt;')
	unfiltered = unfiltered.replace('>', '&gt;')
	return unfiltered

if __name__ == '__main__':
	print('TAXSS Demo')
	unfiltered = input('Enter XSS string: ')
	filtered = sanitize_xss(unfiltered)
	print(filtered)