import taxss

def test_lt_gt():
	sanitized = taxss.sanitize_xss('<script>alert(1)</script>')
	assert sanitized == '&lt;script&gt;alert(1)&lt;/script&gt;'