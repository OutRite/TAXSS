import taxss

def test_script_tag_removal():
	sanitized = taxss.sanitize_xss('<script>alert(1)</script>')
	assert sanitized == 'alert(1)'

def test_script_tag_removal_withtext():
	sanitized = taxss.sanitize_xss('hello <script>alert(1)</script>world')
	assert sanitized == 'hello alert(1)world'

def test_img_ontag_removal():
	sanitized = taxss.sanitize_xss('<img src=x onerror=alert(1)>')
	assert sanitized == ''

def test_img_ontag_removal_withtext():
	sanitized = taxss.sanitize_xss('hello <img src=x onerror=alert(1)>world')
	assert sanitized == 'hello world'