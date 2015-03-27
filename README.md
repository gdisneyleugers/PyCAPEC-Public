# PyCAPEC-Public
PyCAPEC CAPEC/CWE Mapper and Graphiz visualization tool.
# To Run
./Runner.sh
Example XSS:
Gregorys-MacBook-Pro:PyCAPEC gdl$ ./Runner.sh 
Search: XSS
|===========================================|
  CAPEC: 
|===========================================|
CAPEC: 
    "ID": "86",
    "Name": "Embedding Script (XSS) in HTTP Headers",
    "Pattern_Abstraction": "Detailed",
    "Pattern_Completeness": "Complete",
    "Status": "Draft"

|===========================================|
CAPEC: 
    "ID": "91",
    "Name": "XSS in IMG Tags",
    "Pattern_Abstraction": "Detailed",
    "Pattern_Completeness": "Complete",
    "Status": "Draft"

|===========================================|
  CWE: 
|===========================================|
CWE: 
    "ID": "712",
    "Name": "OWASP Top Ten 2007 Category A1 - Cross Site Scripting (XSS)",
    "Status": "Incomplete"

|===========================================|
CWE: 
    "ID": "725",
    "Name": "OWASP Top Ten 2004 Category A4 - Cross-Site Scripting (XSS) Flaws",
    "Status": "Incomplete"

|===========================================|
CWE: 
    "ID": "811",
    "Name": "OWASP Top Ten 2010 Category A2 - Cross-Site Scripting (XSS)",
    "Status": "Incomplete"

|===========================================|
CWE: 
    "ID": "931",
    "Name": "OWASP Top Ten 2013 Category A3 - Cross-Site Scripting (XSS)",
    "Status": "Incomplete"

|===========================================|
CWE: 
    "ID": "80",
    "Name": "Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)",
    "Status": "Incomplete",
    "Weakness_Abstraction": "Variant"

|===========================================|
CWE: 
    "ID": "85",
    "Name": "Doubled Character XSS Manipulations",
    "Status": "Draft",
    "Weakness_Abstraction": "Variant"

|===========================================|
CWE: 
    "ID": "87",
    "Name": "Improper Neutralization of Alternate XSS Syntax",
    "Status": "Draft",
    "Weakness_Abstraction": "Variant"

|===========================================|

This also creates a graphviz file creating a visualization of CAPEC/CWE labels.
cat tm-XSS.gv
// XSS
digraph{ 
    "CAPEC" ->  "86"
    "86" ->  "Embedding Script (XSS) in HTTP Headers"

    "CAPEC" ->  "91"
    "91" ->  "XSS in IMG Tags"

    "CWE" ->  "712"
    "712" ->  "OWASP Top Ten 2007 Category A1 - Cross Site Scripting (XSS)"

    "CWE" ->  "725"
    "725" ->  "OWASP Top Ten 2004 Category A4 - Cross-Site Scripting (XSS) Flaws"

    "CWE" ->  "811"
    "811" ->  "OWASP Top Ten 2010 Category A2 - Cross-Site Scripting (XSS)"

    "CWE" ->  "931"
    "931" ->  "OWASP Top Ten 2013 Category A3 - Cross-Site Scripting (XSS)"

    "CWE" ->  "80"
    "80" ->  "Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)"

    "CWE" ->  "85"
    "85" ->  "Doubled Character XSS Manipulations"

    "CWE" ->  "87"
    "87" ->  "Improper Neutralization of Alternate XSS Syntax"
}
