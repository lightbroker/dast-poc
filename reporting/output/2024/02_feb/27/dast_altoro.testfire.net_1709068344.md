# ZAP Scanning Report


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 1 |
| Medium | 5 |
| Low | 5 |
| Informational | 10 |




## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Cross Site Scripting (DOM Based) | High | 3 |
| Absence of Anti-CSRF Tokens | Medium | 2 |
| Anti-CSRF Tokens Check | Medium | 3 |
| Content Security Policy (CSP) Header Not Set | Medium | 2 |
| Missing Anti-clickjacking Header | Medium | 2 |
| Relative Path Confusion | Medium | 1 |
| Cookie Slack Detector | Low | 2 |
| Cookie without SameSite Attribute | Low | 1 |
| Permissions Policy Header Not Set | Low | 2 |
| Server Leaks Version Information via "Server" HTTP Response Header Field | Low | 2 |
| X-Content-Type-Options Header Missing | Low | 2 |
| Cookie Slack Detector | Informational | 1 |
| GET for POST | Informational | 1 |
| Possible Username Enumeration | Informational | 2 |
| Sec-Fetch-Dest Header is Missing | Informational | 2 |
| Sec-Fetch-Mode Header is Missing | Informational | 2 |
| Sec-Fetch-Site Header is Missing | Informational | 2 |
| Sec-Fetch-User Header is Missing | Informational | 2 |
| Session Management Response Identified | Informational | 3 |
| Storable and Cacheable Content | Informational | 2 |
| User Agent Fuzzer | Informational | 12 |




## Alert Detail



### [ Cross Site Scripting (DOM Based) ](https://www.zaproxy.org/docs/alerts/40026/)



##### High (High)

### Description

Cross-site Scripting (XSS) is an attack technique that involves echoing attacker-supplied code into a user's browser instance. A browser instance can be a standard web browser client, or a browser object embedded in a software product such as the browser within WinAmp, an RSS reader, or an email client. The code itself is usually written in HTML/JavaScript, but may also extend to VBScript, ActiveX, Java, Flash, or any other browser-supported technology.
When an attacker gets a user's browser to execute his/her code, the code will run within the security context (or zone) of the hosting web site. With this level of privilege, the code has the ability to read, modify and transmit any sensitive data accessible by the browser. A Cross-site Scripted user could have his/her account hijacked (cookie theft), their browser redirected to another location, or possibly shown fraudulent content delivered by the web site they are visiting. Cross-site Scripting attacks essentially compromise the trust relationship between a user and the web site. Applications utilizing browser object instances which load content from the file system may execute code under the local machine zone allowing for system compromise.

There are three types of Cross-site Scripting attacks: non-persistent, persistent and DOM-based.
Non-persistent attacks and DOM-based attacks require a user to either visit a specially crafted link laced with malicious code, or visit a malicious web page containing a web form, which when posted to the vulnerable site, will mount the attack. Using a malicious form will oftentimes take place when the vulnerable resource only accepts HTTP POST requests. In such a case, the form can be submitted automatically, without the victim's knowledge (e.g. by using JavaScript). Upon clicking on the malicious link or submitting the malicious form, the XSS payload will get echoed back and will get interpreted by the user's browser and execute. Another technique to send almost arbitrary requests (GET and POST) is by using an embedded client, such as Adobe Flash.
Persistent attacks occur when the malicious code is submitted to a web site where it's stored for a period of time. Examples of an attacker's favorite targets often include message board posts, web mail messages, and web chat software. The unsuspecting user is not required to interact with any additional site/link (e.g. an attacker site or a malicious link sent via email), just simply view the web page containing the code.

* URL: http://altoro.testfire.net/login.jsp%3Fname=abc%23%3Cimg%20src=%22random.gif%22%20onerror=alert(5397&29%3E
  * Method: `GET`
  * Parameter: ``
  * Attack: `?name=abc#<img src="random.gif" onerror=alert(5397)>`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `
* URL: http://altoro.testfire.net%3Fname=abc%23%3Cimg%20src=%22random.gif%22%20onerror=alert(5397&29%3E
  * Method: `GET`
  * Parameter: ``
  * Attack: `?name=abc#<img src="random.gif" onerror=alert(5397)>`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `
* URL: http://altoro.testfire.net/doLogin%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `POST`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `

Instances: 3

### Solution

Phase: Architecture and Design
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
Examples of libraries and frameworks that make it easier to generate properly encoded output include Microsoft's Anti-XSS library, the OWASP ESAPI Encoding module, and Apache Wicket.

Phases: Implementation; Architecture and Design
Understand the context in which your data will be used and the encoding that will be expected. This is especially important when transmitting data between different components, or when generating outputs that can contain multiple encodings at the same time, such as web pages or multi-part mail messages. Study all expected communication protocols and data representations to determine the required encoding strategies.
For any data that will be output to another web page, especially any data that was received from external inputs, use the appropriate encoding on all non-alphanumeric characters.
Consult the XSS Prevention Cheat Sheet for more details on the types of encoding and escaping that are needed.

Phase: Architecture and Design
For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.

If available, use structured mechanisms that automatically enforce the separation between data and code. These mechanisms may be able to provide the relevant quoting, encoding, and validation automatically, instead of relying on the developer to provide this capability at every point where output is generated.

Phase: Implementation
For every web page that is generated, use and specify a character encoding such as ISO-8859-1 or UTF-8. When an encoding is not specified, the web browser may choose a different encoding by guessing which encoding is actually being used by the web page. This can cause the web browser to treat certain sequences as special, opening up the client to subtle XSS attacks. See CWE-116 for more mitigations related to encoding/escaping.

To help mitigate XSS attacks against the user's session cookie, set the session cookie to be HttpOnly. In browsers that support the HttpOnly feature (such as more recent versions of Internet Explorer and Firefox), this attribute can prevent the user's session cookie from being accessible to malicious client-side scripts that use document.cookie. This is not a complete solution, since HttpOnly is not supported by all browsers. More importantly, XMLHTTPRequest and other powerful browser technologies provide read access to HTTP headers, including the Set-Cookie header in which the HttpOnly flag is set.

Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use an allow list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. Do not rely exclusively on looking for malicious or malformed inputs (i.e., do not rely on a deny list). However, deny lists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if you are expecting colors such as "red" or "blue."

Ensure that you perform input validation at well-defined interfaces within the application. This will help protect the application even if a component is reused or moved elsewhere.
	

### Reference


* [ https://owasp.org/www-community/attacks/xss/ ](https://owasp.org/www-community/attacks/xss/)
* [ https://cwe.mitre.org/data/definitions/79.html ](https://cwe.mitre.org/data/definitions/79.html)


#### CWE Id: [ 79 ](https://cwe.mitre.org/data/definitions/79.html)


#### WASC Id: 8

#### Source ID: 1

### [ Absence of Anti-CSRF Tokens ](https://www.zaproxy.org/docs/alerts/10202/)



##### Medium (Low)

### Description

No Anti-CSRF tokens were found in a HTML submission form.
A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.

CSRF attacks are effective in a number of situations, including:
    * The victim has an active session on the target site.
    * The victim is authenticated via HTTP auth on the target site.
    * The victim is on the same local network as the target site.

CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form id="frmSearch" method="get" action="/search.jsp">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "query" ].`
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form id="frmSearch" method="get" action="/search.jsp">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "query" ].`

Instances: 2

### Solution

Phase: Architecture and Design
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
For example, use anti-CSRF packages such as the OWASP CSRFGuard.

Phase: Implementation
Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.

Phase: Architecture and Design
Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330).
Note that this can be bypassed using XSS.

Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.
Note that this can be bypassed using XSS.

Use the ESAPI Session Management control.
This control includes a component for CSRF.

Do not use the GET method for any request that triggers a state change.

Phase: Implementation
Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [ https://cwe.mitre.org/data/definitions/352.html ](https://cwe.mitre.org/data/definitions/352.html)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Anti-CSRF Tokens Check ](https://www.zaproxy.org/docs/alerts/20012/)



##### Medium (Medium)

### Description

A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.

CSRF attacks are effective in a number of situations, including:
    * The victim has an active session on the target site.
    * The victim is authenticated via HTTP auth on the target site.
    * The victim is on the same local network as the target site.

CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form id="frmSearch" method="get" action="/search.jsp">`
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="doLogin" method="post" name="login" id="login" onsubmit="return (confirminput(login));">`
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form id="frmSearch" method="get" action="/search.jsp">`
  * Other Info: ``

Instances: 3

### Solution

Phase: Architecture and Design
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
For example, use anti-CSRF packages such as the OWASP CSRFGuard.

Phase: Implementation
Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.

Phase: Architecture and Design
Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330).
Note that this can be bypassed using XSS.

Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.
Note that this can be bypassed using XSS.

Use the ESAPI Session Management control.
This control includes a component for CSRF.

Do not use the GET method for any request that triggers a state change.

Phase: Implementation
Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [ https://cwe.mitre.org/data/definitions/352.html ](https://cwe.mitre.org/data/definitions/352.html)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 1

### [ Content Security Policy (CSP) Header Not Set ](https://www.zaproxy.org/docs/alerts/10038/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 2

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy ](https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy)
* [ https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://w3c.github.io/webappsec-csp/ ](https://w3c.github.io/webappsec-csp/)
* [ https://web.dev/articles/csp ](https://web.dev/articles/csp)
* [ https://caniuse.com/#feat=contentsecuritypolicy ](https://caniuse.com/#feat=contentsecuritypolicy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Missing Anti-clickjacking Header ](https://www.zaproxy.org/docs/alerts/10020/)



##### Medium (Medium)

### Description

The response does not include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options to protect against 'ClickJacking' attacks.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 2

### Solution

Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.
If you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)


#### CWE Id: [ 1021 ](https://cwe.mitre.org/data/definitions/1021.html)


#### WASC Id: 15

#### Source ID: 3

### [ Relative Path Confusion ](https://www.zaproxy.org/docs/alerts/10051/)



##### Medium (Medium)

### Description

The web server is configured to serve responses to ambiguous URLs in a manner that is likely to lead to confusion about the correct "relative path" for the URL. Resources (CSS, images, etc.) are also specified in the page response using relative, rather than absolute URLs. In an attack, if the web browser parses the "cross-content" response in a permissive manner, or can be tricked into permissively parsing the "cross-content" response, using techniques such as framing, then the web browser may be fooled into interpreting HTML as CSS (or other content types), leading to an XSS vulnerability.

* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: ``
  * Attack: `http://altoro.testfire.net/login.jsp/nsaxs/uj9ll`
  * Evidence: `<a id="CatLink1" class="subheader" href="index.jsp?content=personal.htm">PERSONAL</a>`
  * Other Info: `No <base> tag was specified in the HTML <head> tag to define the location for relative URLs.
A Content Type of "text/html;charset=ISO-8859-1" was specified. If the web browser is employing strict parsing rules, this will prevent cross-content attacks from succeeding. Quirks Mode in the web browser would disable strict parsing.  
Quirks Mode is implicitly enabled via the use of an old DOCTYPE with PUBLIC id "-//W3C//DTD XHTML 1.0 Transitional//EN", allowing the specified Content Type to be bypassed in some web browsers.`

Instances: 1

### Solution

Web servers and frameworks should be updated to be configured to not serve responses to ambiguous URLs in such a way that the relative path of such URLs could be mis-interpreted by components on either the client side, or server side.
Within the application, the correct use of the "<base>" HTML tag in the HTTP response will unambiguously specify the base URL for all relative URLs in the document.
Use the "Content-Type" HTTP response header to make it harder for the attacker to force the web browser to mis-interpret the content type of the response.
Use the "X-Content-Type-Options: nosniff" HTTP response header to prevent the web browser from "sniffing" the content type of the response.
Use a modern DOCTYPE such as "<!doctype html>" to prevent the page from being rendered in the web browser using "Quirks Mode", since this results in the content type being ignored by the web browser.
Specify the "X-Frame-Options" HTTP response header to prevent Quirks Mode from being enabled in the web browser using framing attacks. 

### Reference


* [ https://arxiv.org/abs/1811.00917 ](https://arxiv.org/abs/1811.00917)
* [ https://hsivonen.fi/doctype/ ](https://hsivonen.fi/doctype/)
* [ https://www.w3schools.com/tags/tag_base.asp ](https://www.w3schools.com/tags/tag_base.asp)


#### CWE Id: [ 20 ](https://cwe.mitre.org/data/definitions/20.html)


#### WASC Id: 20

#### Source ID: 1

### [ Cookie Slack Detector ](https://www.zaproxy.org/docs/alerts/90027/)



##### Low (Low)

### Description

Repeated GET requests: drop a different cookie each time, followed by normal request with all cookies to stabilize session, compare responses against original baseline GET. This can reveal areas where cookie based authentication/attributes are not actually enforced.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `NOTE: Because of its name this cookie may be important, but dropping it appears to have no effect: [JSESSIONID] 
Cookies that don't have expected effects can reveal flaws in application logic. In the worst case, this can reveal where authentication via cookie token(s) is not actually enforced.
These cookies affected the response: 
These cookies did NOT affect the response: AltoroAccounts,JSESSIONID
`
* URL: http://altoro.testfire.net/doLogin
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `NOTE: Because of its name this cookie may be important, but dropping it appears to have no effect: [JSESSIONID] 
Cookies that don't have expected effects can reveal flaws in application logic. In the worst case, this can reveal where authentication via cookie token(s) is not actually enforced.
These cookies affected the response: 
These cookies did NOT affect the response: AltoroAccounts,JSESSIONID
`

Instances: 2

### Solution



### Reference


* [ https://cwe.mitre.org/data/definitions/205.html ](https://cwe.mitre.org/data/definitions/205.html)


#### CWE Id: [ 200 ](https://cwe.mitre.org/data/definitions/200.html)


#### WASC Id: 45

#### Source ID: 1

### [ Cookie without SameSite Attribute ](https://www.zaproxy.org/docs/alerts/10054/)



##### Low (Medium)

### Description

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a 'cross-site' request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: `JSESSIONID`
  * Attack: ``
  * Evidence: `Set-Cookie: JSESSIONID`
  * Other Info: ``

Instances: 1

### Solution

Ensure that the SameSite attribute is set to either 'lax' or ideally 'strict' for all cookies.

### Reference


* [ https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site ](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site)


#### CWE Id: [ 1275 ](https://cwe.mitre.org/data/definitions/1275.html)


#### WASC Id: 13

#### Source ID: 3

### [ Permissions Policy Header Not Set ](https://www.zaproxy.org/docs/alerts/10063/)



##### Low (Medium)

### Description

Permissions Policy Header is an added layer of security that helps to restrict from unauthorized access or usage of browser/client features by web resources. This policy ensures the user privacy by limiting or specifying the features of the browsers can be used by the web resources. Permissions Policy provides a set of standard HTTP headers that allow website owners to limit which features of browsers can be used by the page such as camera, microphone, location, full screen etc.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 2

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy)
* [ https://developer.chrome.com/blog/feature-policy/ ](https://developer.chrome.com/blog/feature-policy/)
* [ https://scotthelme.co.uk/a-new-security-header-feature-policy/ ](https://scotthelme.co.uk/a-new-security-header-feature-policy/)
* [ https://w3c.github.io/webappsec-feature-policy/ ](https://w3c.github.io/webappsec-feature-policy/)
* [ https://www.smashingmagazine.com/2018/12/feature-policy/ ](https://www.smashingmagazine.com/2018/12/feature-policy/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Server Leaks Version Information via "Server" HTTP Response Header Field ](https://www.zaproxy.org/docs/alerts/10036/)



##### Low (High)

### Description

The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Apache-Coyote/1.1`
  * Other Info: ``
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Apache-Coyote/1.1`
  * Other Info: ``

Instances: 2

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.

### Reference


* [ https://httpd.apache.org/docs/current/mod/core.html#servertokens ](https://httpd.apache.org/docs/current/mod/core.html#servertokens)
* [ https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10) ](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10))
* [ https://www.troyhunt.com/shhh-dont-let-your-response-headers/ ](https://www.troyhunt.com/shhh-dont-let-your-response-headers/)


#### CWE Id: [ 200 ](https://cwe.mitre.org/data/definitions/200.html)


#### WASC Id: 13

#### Source ID: 3

### [ X-Content-Type-Options Header Missing ](https://www.zaproxy.org/docs/alerts/10021/)



##### Low (Medium)

### Description

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`

Instances: 2

### Solution

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### Reference


* [ https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85) ](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85))
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Cookie Slack Detector ](https://www.zaproxy.org/docs/alerts/90027/)



##### Informational (Low)

### Description

Repeated GET requests: drop a different cookie each time, followed by normal request with all cookies to stabilize session, compare responses against original baseline GET. This can reveal areas where cookie based authentication/attributes are not actually enforced.

* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `Dropping this cookie appears to have invalidated the session: [JSESSIONID] A follow-on request with all original cookies still had a different response than the original request. 
`

Instances: 1

### Solution



### Reference


* [ https://cwe.mitre.org/data/definitions/205.html ](https://cwe.mitre.org/data/definitions/205.html)


#### CWE Id: [ 200 ](https://cwe.mitre.org/data/definitions/200.html)


#### WASC Id: 45

#### Source ID: 1

### [ GET for POST ](https://www.zaproxy.org/docs/alerts/10058/)



##### Informational (High)

### Description

A request that was originally observed as a POST was also accepted as a GET. This issue does not represent a security weakness unto itself, however, it may facilitate simplification of other attacks. For example if the original POST is subject to Cross-Site Scripting (XSS), then this finding may indicate that a simplified (GET based) XSS may also be possible.

* URL: http://altoro.testfire.net/doLogin
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `GET http://altoro.testfire.net/doLogin?btnSubmit=Login&passw=admin&uid=admin HTTP/1.1`
  * Other Info: ``

Instances: 1

### Solution

Ensure that only POST is accepted where POST is expected.

### Reference



#### CWE Id: [ 16 ](https://cwe.mitre.org/data/definitions/16.html)


#### WASC Id: 20

#### Source ID: 1

### [ Possible Username Enumeration ](https://www.zaproxy.org/docs/alerts/40023/)



##### Informational (Low)

### Description

It may be possible to enumerate usernames, based on differing HTTP responses when valid and invalid usernames are provided. This would greatly increase the probability of success of password brute-forcing attacks against the system. Note that false positives may sometimes be minimised by increasing the 'Attack Strength' Option in ZAP.  Please manually check the 'Other Info' field to confirm if this is actually an issue. 

* URL: http://altoro.testfire.net/doLogin
  * Method: `POST`
  * Parameter: `passw`
  * Attack: `Manipulate [form] field: [passw] and monitor the output `
  * Evidence: ``
  * Other Info: `[form] parameter [passw] leaks information on whether a user exists. The [14] differences in output, for the valid original username value [admin], and invalid username value [snfvm] are:
[
(Changed Text)
Output for Valid Username  : [position: 1, size: 1, lines: [Location: /bank/main.jsp]]

Output for Invalid Username: [position: 1, size: 1, lines: [Location: login.jsp]]

(Changed Text)
Output for Valid Username  : [position: 5, size: 1, lines: [Content-Length: XXXX]]

Output for Invalid Username: [position: 5, size: 1, lines: [content-length: 8459]]

(Changed Text)
Output for Valid Username  : [position: 58, size: 1, lines: [	<!-- MEMBER TOC BEGIN -->]]

Output for Invalid Username: [position: 58, size: 1, lines: [	 ]]

(Changed Text)
Output for Valid Username  : [position: 60, size: 1, lines: [ ]]

Output for Invalid Username: [position: 60, size: 13, lines: [<!-- TOC BEGIN -->     ,      <td valign="top" class="cc br bb">,         <br style="line-height: 10px;"/>,         ,         <a id="CatLink1" class="subheader" href="index.jsp?content=YYYY">PERSONAL</a>,         <ul class="sidebar">,             <li><a id="MenuHyperLink1" href="index.jsp?content=YYYY">Deposit Product</a></li>,             <li><a id="MenuHyperLink2" href="index.jsp?content=YYYY">Checking</a></li>,             <li><a id="MenuHyperLink3" href="index.jsp?content=YYYY">Loan Products</a></li>,             <li><a id="MenuHyperLink4" href="index.jsp?content=YYYY">Cards</a></li>,             <li><a id="MenuHyperLink5" href="index.jsp?content=YYYY">Investments &amp; Insurance</a></li>,             <li><a id="MenuHyperLink6" href="index.jsp?content=YYYY">Other Services</a></li>,         </ul>]]

(Inserted text)
Output for Valid Username  : [position: 62, size: 0, lines: []]

Output for Invalid Username: [position: 74, size: 9, lines: [        <a id="CatLink2" class="subheader" href="index.jsp?content=YYYY">SMALL BUSINESS</a>,         <ul class="sidebar">,             <li><a id="MenuHyperLink7" href="index.jsp?content=YYYY">Deposit Products</a></li>,             <li><a id="MenuHyperLink8" href="index.jsp?content=YYYY">Lending Services</a></li>,             <li><a id="MenuHyperLink9" href="index.jsp?content=YYYY">Cards</a></li>,             <li><a id="MenuHyperLink10" href="index.jsp?content=YYYY">Insurance</a></li>,             <li><a id="MenuHyperLink11" href="index.jsp?content=YYYY">Retirement</a></li>,             <li><a id="MenuHyperLink12" href="index.jsp?content=YYYY">Other Services</a></li>,         </ul>]]

(Changed Text)
Output for Valid Username  : [position: 63, size: 7, lines: [, <table cellspacing="0" width="100%">, , ,     <td valign="top" class="cc br bb">,         <br style="line-height: 10px;"/>,         <b>I WANT TO ...</b>]]

Output for Invalid Username: [position: 84, size: 1, lines: [        <a id="CatLink3" class="subheader" href="index.jsp?content=YYYY">INSIDE ALTORO MUTUAL</a>]]

(Changed Text)
Output for Valid Username  : [position: 71, size: 7, lines: [            <li><a id="MenuHyperLink1" href="/bank/main.jsp">View Account Summary</a></li>,             <li><a id="MenuHyperLink2" href="/bank/transaction.jsp">View Recent Transactions</a></li>,             <li><a id="MenuHyperLink3" href="/bank/transfer.jsp">Transfer Funds</a></li>, 	 		<!-- <li><a id="MenuHyperLink3" href="/bank/stocks.jsp">Trade Stocks</a></li>-->, 	 		 ,             <li><a id="MenuHyperLink4" href="/bank/queryxpath.jsp">Search News Articles</a></li>,             <li><a id="MenuHyperLink5" href="/bank/customize.jsp">Customize Site Language</a></li>]]

Output for Invalid Username: [position: 86, size: 7, lines: [            <li><a id="MenuHyperLink13" href="index.jsp?content=YYYY">About Us</a></li>,             <li><a id="MenuHyperLink14" href="index.jsp?content=YYYY">Contact Us</a></li>,             <li><a id="MenuHyperLink15" href="cgi.exe">Locations</a></li>,             <li><a id="MenuHyperLink16" href="index.jsp?content=YYYY">Investor Relations</a></li>,             <li><a id="MenuHyperLink17" href="index.jsp?content=YYYY">Press Room</a></li>,             <li><a id="MenuHyperLink18" href="index.jsp?content=YYYY">Careers</a></li>, 			<li><a id="MenuHyperLink19" href="subscribe.jsp">Subscribe</a></li>]]

(Deleted Text)
Output for Valid Username  : [position: 79, size: 10, lines: [		, 		<span id="_ctl0__ctl0_Content_Administration">, 			<br style="line-height: 10px;"/>, 			<b>ADMINISTRATION</b>, 			<ul class="sidebar">, 				<li><a href="/admin/admin.jsp">Edit Users</a></li>, 			 , 			</ul>, 		</span>, 		]]

Output for Invalid Username: [position: 94, size: 0, lines: []]

(Changed Text)
Output for Valid Username  : [position: 90, size: 3, lines: [<!-- MEMBER TOC END -->, 	<td valign="top" colspan="3" class="bb">, 		]]

Output for Invalid Username: [position: 95, size: 3, lines: [<!-- TOC END -->, ,    <td valign="top" colspan="3" class="bb">]]

(Inserted text)
Output for Valid Username  : [position: 95, size: 0, lines: []]

Output for Invalid Username: [position: 100, size: 1, lines: [		<h1>Online Banking Login</h1>]]

(Inserted text)
Output for Valid Username  : [position: 96, size: 0, lines: []]

Output for Invalid Username: [position: 102, size: 4, lines: [		<!-- To get the latest admin login, please contact SiteOps at 415-555-6159 -->, 		<p><span id="_ctl0__ctl0_Content_Main_message" style="color:#FF0066;font-size:12pt;font-weight:bold;">, 		Login Failed: We're sorry, but this username or password was not found in our system. Please try again., 		</span></p>]]

(Changed Text)
Output for Valid Username  : [position: 97, size: 24, lines: [		<h1>Hello Admin User, 		  </h1>, 		, 		<p>, 		  Welcome to Altoro Mutual Online., 		</p>, 		, 		<form name="details" method="get" action="showAccount">, 		<table border="0">, 		  <TR valign="top">, 		    <td>View Account Details:</td>, 		    <td align="left">, 			  <select size="1" name="listAccounts" id="listAccounts">, 				<option value="800000" >800000 Corporate</option>, <option value="800001" >800001 Checking</option>, , 			  </select>, 		      <input type="submit" id="btnGetAccount" value="   GO   ">, 		    </td>, 		  </tr>, 		  <tr>, 		    <td colspan="2"><span id="_ctl0__ctl0_Content_Main_promo"><table width=590 border=0><tr><td><h2>Congratulations! </h2></td></tr><tr><td>You have been pre-approved for an Altoro Gold Visa with a credit limit of $10000!</td></tr><tr><td>Click <a href='apply.jsp'>Here</a> to apply.</td></tr></table></span></td>, 		  </tr>, 		</table>]]

Output for Invalid Username: [position: 107, size: 27, lines: [		<form action="doLogin" method="post" name="login" id="login" onsubmit="return (confirminput(login));">, 		  <table>, 		    <tr>, 		      <td>, 		        Username:, 		      </td>, 		      <td>, 		        <input type="text" id="uid" name="uid" value="" style="width: 150px;">, 		      </td>, 		      <td>, 		      </td>, 		    </tr>, 		    <tr>, 		      <td>, 		        Password:, 		      </td>, 		      <td>, 		        <input type="password" id="passw" name="passw" style="width: 150px;">, 		        </td>, 		    </tr>, 		    <tr>, 		        <td></td>, 		        <td>, 		          <input type="submit" name="btnSubmit" value="Login">, 		        </td>, 		      </tr>, 		  </table>]]

(Inserted text)
Output for Valid Username  : [position: 124, size: 0, lines: []]

Output for Invalid Username: [position: 137, size: 26, lines: [		, 		<script type="text/javascript">, 			function setfocus() {, 			    if (document.login.uid.value=="") {, 			      	document.login.uid.focus();, 			    } else {, 			      	document.login.passw.focus();, 			    }, 			}, 			, 			function confirminput(myform) {, 			    if (myform.uid.value.length && myform.passw.value.length) {, 			      return (true);, 			    } else if (!(myform.uid.value.length)) {, 			      myform.reset();, 			      myform.uid.focus();, 			      alert ("You must enter a valid username");, 			      return (false);, 			    } else {, 			      myform.passw.focus();, 			      alert ("You must enter a valid password");, 			      return (false);, 			    }, 			}, 			window.onload = setfocus;, 		</script>]]

(Changed Text)
Output for Valid Username  : [position: 162, size: 1, lines: [<!-- END FOOTER -->	]]

Output for Invalid Username: [position: 201, size: 1, lines: [<!-- END FOOTER -->]]
]`
* URL: http://altoro.testfire.net/doLogin
  * Method: `POST`
  * Parameter: `uid`
  * Attack: `Manipulate [form] field: [uid] and monitor the output `
  * Evidence: ``
  * Other Info: `[form] parameter [uid] leaks information on whether a user exists. The [14] differences in output, for the valid original username value [admin], and invalid username value [xeoee] are:
[
(Changed Text)
Output for Valid Username  : [position: 1, size: 1, lines: [Location: /bank/main.jsp]]

Output for Invalid Username: [position: 1, size: 1, lines: [Location: login.jsp]]

(Changed Text)
Output for Valid Username  : [position: 5, size: 1, lines: [Content-Length: XXXX]]

Output for Invalid Username: [position: 5, size: 1, lines: [content-length: 8459]]

(Changed Text)
Output for Valid Username  : [position: 58, size: 1, lines: [	<!-- MEMBER TOC BEGIN -->]]

Output for Invalid Username: [position: 58, size: 1, lines: [	 ]]

(Changed Text)
Output for Valid Username  : [position: 60, size: 1, lines: [ ]]

Output for Invalid Username: [position: 60, size: 13, lines: [<!-- TOC BEGIN -->     ,      <td valign="top" class="cc br bb">,         <br style="line-height: 10px;"/>,         ,         <a id="CatLink1" class="subheader" href="index.jsp?content=YYYY">PERSONAL</a>,         <ul class="sidebar">,             <li><a id="MenuHyperLink1" href="index.jsp?content=YYYY">Deposit Product</a></li>,             <li><a id="MenuHyperLink2" href="index.jsp?content=YYYY">Checking</a></li>,             <li><a id="MenuHyperLink3" href="index.jsp?content=YYYY">Loan Products</a></li>,             <li><a id="MenuHyperLink4" href="index.jsp?content=YYYY">Cards</a></li>,             <li><a id="MenuHyperLink5" href="index.jsp?content=YYYY">Investments &amp; Insurance</a></li>,             <li><a id="MenuHyperLink6" href="index.jsp?content=YYYY">Other Services</a></li>,         </ul>]]

(Inserted text)
Output for Valid Username  : [position: 62, size: 0, lines: []]

Output for Invalid Username: [position: 74, size: 9, lines: [        <a id="CatLink2" class="subheader" href="index.jsp?content=YYYY">SMALL BUSINESS</a>,         <ul class="sidebar">,             <li><a id="MenuHyperLink7" href="index.jsp?content=YYYY">Deposit Products</a></li>,             <li><a id="MenuHyperLink8" href="index.jsp?content=YYYY">Lending Services</a></li>,             <li><a id="MenuHyperLink9" href="index.jsp?content=YYYY">Cards</a></li>,             <li><a id="MenuHyperLink10" href="index.jsp?content=YYYY">Insurance</a></li>,             <li><a id="MenuHyperLink11" href="index.jsp?content=YYYY">Retirement</a></li>,             <li><a id="MenuHyperLink12" href="index.jsp?content=YYYY">Other Services</a></li>,         </ul>]]

(Changed Text)
Output for Valid Username  : [position: 63, size: 7, lines: [, <table cellspacing="0" width="100%">, , ,     <td valign="top" class="cc br bb">,         <br style="line-height: 10px;"/>,         <b>I WANT TO ...</b>]]

Output for Invalid Username: [position: 84, size: 1, lines: [        <a id="CatLink3" class="subheader" href="index.jsp?content=YYYY">INSIDE ALTORO MUTUAL</a>]]

(Changed Text)
Output for Valid Username  : [position: 71, size: 7, lines: [            <li><a id="MenuHyperLink1" href="/bank/main.jsp">View Account Summary</a></li>,             <li><a id="MenuHyperLink2" href="/bank/transaction.jsp">View Recent Transactions</a></li>,             <li><a id="MenuHyperLink3" href="/bank/transfer.jsp">Transfer Funds</a></li>, 	 		<!-- <li><a id="MenuHyperLink3" href="/bank/stocks.jsp">Trade Stocks</a></li>-->, 	 		 ,             <li><a id="MenuHyperLink4" href="/bank/queryxpath.jsp">Search News Articles</a></li>,             <li><a id="MenuHyperLink5" href="/bank/customize.jsp">Customize Site Language</a></li>]]

Output for Invalid Username: [position: 86, size: 7, lines: [            <li><a id="MenuHyperLink13" href="index.jsp?content=YYYY">About Us</a></li>,             <li><a id="MenuHyperLink14" href="index.jsp?content=YYYY">Contact Us</a></li>,             <li><a id="MenuHyperLink15" href="cgi.exe">Locations</a></li>,             <li><a id="MenuHyperLink16" href="index.jsp?content=YYYY">Investor Relations</a></li>,             <li><a id="MenuHyperLink17" href="index.jsp?content=YYYY">Press Room</a></li>,             <li><a id="MenuHyperLink18" href="index.jsp?content=YYYY">Careers</a></li>, 			<li><a id="MenuHyperLink19" href="subscribe.jsp">Subscribe</a></li>]]

(Deleted Text)
Output for Valid Username  : [position: 79, size: 10, lines: [		, 		<span id="_ctl0__ctl0_Content_Administration">, 			<br style="line-height: 10px;"/>, 			<b>ADMINISTRATION</b>, 			<ul class="sidebar">, 				<li><a href="/admin/admin.jsp">Edit Users</a></li>, 			 , 			</ul>, 		</span>, 		]]

Output for Invalid Username: [position: 94, size: 0, lines: []]

(Changed Text)
Output for Valid Username  : [position: 90, size: 3, lines: [<!-- MEMBER TOC END -->, 	<td valign="top" colspan="3" class="bb">, 		]]

Output for Invalid Username: [position: 95, size: 3, lines: [<!-- TOC END -->, ,    <td valign="top" colspan="3" class="bb">]]

(Inserted text)
Output for Valid Username  : [position: 95, size: 0, lines: []]

Output for Invalid Username: [position: 100, size: 1, lines: [		<h1>Online Banking Login</h1>]]

(Inserted text)
Output for Valid Username  : [position: 96, size: 0, lines: []]

Output for Invalid Username: [position: 102, size: 4, lines: [		<!-- To get the latest admin login, please contact SiteOps at 415-555-6159 -->, 		<p><span id="_ctl0__ctl0_Content_Main_message" style="color:#FF0066;font-size:12pt;font-weight:bold;">, 		Login Failed: We're sorry, but this username or password was not found in our system. Please try again., 		</span></p>]]

(Changed Text)
Output for Valid Username  : [position: 97, size: 24, lines: [		<h1>Hello Admin User, 		  </h1>, 		, 		<p>, 		  Welcome to Altoro Mutual Online., 		</p>, 		, 		<form name="details" method="get" action="showAccount">, 		<table border="0">, 		  <TR valign="top">, 		    <td>View Account Details:</td>, 		    <td align="left">, 			  <select size="1" name="listAccounts" id="listAccounts">, 				<option value="800000" >800000 Corporate</option>, <option value="800001" >800001 Checking</option>, , 			  </select>, 		      <input type="submit" id="btnGetAccount" value="   GO   ">, 		    </td>, 		  </tr>, 		  <tr>, 		    <td colspan="2"><span id="_ctl0__ctl0_Content_Main_promo"><table width=590 border=0><tr><td><h2>Congratulations! </h2></td></tr><tr><td>You have been pre-approved for an Altoro Gold Visa with a credit limit of $10000!</td></tr><tr><td>Click <a href='apply.jsp'>Here</a> to apply.</td></tr></table></span></td>, 		  </tr>, 		</table>]]

Output for Invalid Username: [position: 107, size: 27, lines: [		<form action="doLogin" method="post" name="login" id="login" onsubmit="return (confirminput(login));">, 		  <table>, 		    <tr>, 		      <td>, 		        Username:, 		      </td>, 		      <td>, 		        <input type="text" id="uid" name="uid" value="" style="width: 150px;">, 		      </td>, 		      <td>, 		      </td>, 		    </tr>, 		    <tr>, 		      <td>, 		        Password:, 		      </td>, 		      <td>, 		        <input type="password" id="passw" name="passw" style="width: 150px;">, 		        </td>, 		    </tr>, 		    <tr>, 		        <td></td>, 		        <td>, 		          <input type="submit" name="btnSubmit" value="Login">, 		        </td>, 		      </tr>, 		  </table>]]

(Inserted text)
Output for Valid Username  : [position: 124, size: 0, lines: []]

Output for Invalid Username: [position: 137, size: 26, lines: [		, 		<script type="text/javascript">, 			function setfocus() {, 			    if (document.login.uid.value=="") {, 			      	document.login.uid.focus();, 			    } else {, 			      	document.login.passw.focus();, 			    }, 			}, 			, 			function confirminput(myform) {, 			    if (myform.uid.value.length && myform.passw.value.length) {, 			      return (true);, 			    } else if (!(myform.uid.value.length)) {, 			      myform.reset();, 			      myform.uid.focus();, 			      alert ("You must enter a valid username");, 			      return (false);, 			    } else {, 			      myform.passw.focus();, 			      alert ("You must enter a valid password");, 			      return (false);, 			    }, 			}, 			window.onload = setfocus;, 		</script>]]

(Changed Text)
Output for Valid Username  : [position: 162, size: 1, lines: [<!-- END FOOTER -->	]]

Output for Invalid Username: [position: 201, size: 1, lines: [<!-- END FOOTER -->]]
]`

Instances: 2

### Solution

Do not divulge details of whether a username is valid or invalid. In particular, for unsuccessful login attempts, do not differentiate between an invalid user and an invalid password in the error message, page title, page contents, HTTP headers, or redirection logic.

### Reference


* [ https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account.html ](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account.html)
* [ http://sebastian-schinzel.de/_download/ifip-sec2011.pdf ](http://sebastian-schinzel.de/_download/ifip-sec2011.pdf)


#### CWE Id: [ 200 ](https://cwe.mitre.org/data/definitions/200.html)


#### WASC Id: 13

#### Source ID: 1

### [ Sec-Fetch-Dest Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Specifies how and where the data would be used. For instance, if the value is audio, then the requested resource must be audio data and not any other type of resource.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: `Sec-Fetch-Dest`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: `Sec-Fetch-Dest`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 2

### Solution

Ensure that Sec-Fetch-Dest header is included in request headers.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Dest ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Dest)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Sec-Fetch-Mode Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Allows to differentiate between requests for navigating between HTML pages and requests for loading resources like images, audio etc.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: `Sec-Fetch-Mode`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: `Sec-Fetch-Mode`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 2

### Solution

Ensure that Sec-Fetch-Mode header is included in request headers.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Mode ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Mode)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Sec-Fetch-Site Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Specifies the relationship between request initiator's origin and target's origin.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: `Sec-Fetch-Site`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: `Sec-Fetch-Site`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 2

### Solution

Ensure that Sec-Fetch-Site header is included in request headers.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Sec-Fetch-User Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Specifies if a navigation request was initiated by a user.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: `Sec-Fetch-User`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: `Sec-Fetch-User`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 2

### Solution

Ensure that Sec-Fetch-User header is included in user initiated requests.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-User ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-User)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Session Management Response Identified ](https://www.zaproxy.org/docs/alerts/10112/)



##### Informational (Medium)

### Description

The given response has been identified as containing a session management token. The 'Other Info' field contains a set of header tokens that can be used in the Header Based Session Management Method. If the request is in a context which has a Session Management Method set to "Auto-Detect" then this rule will change the session management to use the tokens identified.

* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: `JSESSIONID`
  * Attack: ``
  * Evidence: `53DDE3C90D080782478FB454CFF1DDA3`
  * Other Info: `
cookie:JSESSIONID`
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `JSESSIONID`
  * Attack: ``
  * Evidence: `73C4D5AECCCCD84EA21E39B10848D041`
  * Other Info: `
cookie:JSESSIONID`
* URL: http://altoro.testfire.net/doLogin
  * Method: `POST`
  * Parameter: `AltoroAccounts`
  * Attack: ``
  * Evidence: `ODAwMDAwfkNvcnBvcmF0ZX4tMi4yMjIyMjIyMjEzMzMzMzMzRTc4fDgwMDAwMX5DaGVja2luZ34yLjIyMjIyMjIyMTMzMzMzMzNFNzh8`
  * Other Info: `
cookie:AltoroAccounts`

Instances: 3

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id)



#### Source ID: 3

### [ Storable and Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users.  If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

* URL: http://altoro.testfire.net
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: http://altoro.testfire.net/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`

Instances: 2

### Solution

Validate that the response does not contain sensitive, personal or user-specific information.  If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user:
Cache-Control: no-cache, no-store, must-revalidate, private
Pragma: no-cache
Expires: 0
This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request. 

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ User Agent Fuzzer ](https://www.zaproxy.org/docs/alerts/10104/)



##### Informational (Medium)

### Description

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3739.0 Safari/537.36 Edg/75.0.109.0`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/91.0`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16`
  * Evidence: ``
  * Other Info: ``
* URL: http://altoro.testfire.net/login.jsp
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `msnbot/1.1 (+http://search.msn.com/msnbot.htm)`
  * Evidence: ``
  * Other Info: ``

Instances: 12

### Solution



### Reference


* [ https://owasp.org/wstg ](https://owasp.org/wstg)



#### Source ID: 1


