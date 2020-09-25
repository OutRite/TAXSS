import taxss

def test_script_tag_removal():
	sanitized = taxss.sanitize_xss('<script>alert(1)</script>')
	assert sanitized == 'alert(1)'

def test_img_ontag_removal():
	sanitized = taxss.sanitize_xss('<img src=x onerror=alert(1)>')
	assert sanitized == '<img src=x >'