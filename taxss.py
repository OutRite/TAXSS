# https://github.com/OutRite/TAXSS
# dont actually use this pls

def clean_tag(unfiltered, tagname):
	begin_offset = unfiltered.find('<' + tagname)
	end_offset = unfiltered.find('</' + tagname)
	if end_offset == -1:
		end_offset = unfiltered.find('>')
	actual_tag_unfiltered = unfiltered[begin_offset:end_offset]
	for i in range(len(bad_attrs)):
		if bad_attrs[i] in actual_tag_unfiltered:
			end_btag_offset = actual_tag_unfiltered.find('>')
			bad_attr_start = actual_tag_unfiltered.find(bad_attrs[i])
			actual_tag_unfiltered = actual_tag_unfiltered[:bad_attr_start] + actual_tag_unfiltered[end_btag_offset:]
	return unfiltered[:begin_offset] + actual_tag_unfiltered + unfiltered[end_offset:]

def sanitize_xss(unfiltered):
	unfiltered = unfiltered.replace('<script>', '')
	unfiltered = unfiltered.replace('</script>', '')
	clean_tag(unfiltered, 'img')
	return unfiltered

if __name__ == '__main__':
	print('TAXSS Demo')
	unfiltered = input('Enter XSS string: ')
	filtered = sanitize_xss(unfiltered)
	print(filtered)