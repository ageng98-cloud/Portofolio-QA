*** Settings ***
Library    RequestsLibrary


*** Variables ***
${BASE_URL}            https://reqres.in
${payload}              {"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver"}
${payload2}             {"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet"}
${payload3}             {"id":2,"email":"","first_name":"","last_name":"Weaver"}
${payload4}             {"id":2,"email":"jane.weaver@reqres.in","first_name":"Janet","last_name":"Weaver"}

#Expect Result
${EXPECTED_id}                2
${EXPECTED_email}             janettt.weaver@reqres.in
${EXPECTED_first_name}        Janet
${EXPECTED_last_name}         Weaver


*** Test Cases ***


MethodGET                   #Positve Case GET API
    [Documentation]    Test GET request to the API
    Create Session    Base    ${BASE_URL}
    ${headers}=    Create Dictionary    Content-Type    application/json
    ${response}=    GET On Session    Base    /api/users    headers=${headers}  data=${payload}
    
    Log    ${response.status_code}
    Log    ${response.json()}
    
    #Check Status 
    Should Be Equal As Strings    ${response.status_code}    200

    #Check Field 
    ${json_response}=    Set Variable    ${response.json()}
        
    Delete All Sessions

Method-GETPer-ID            #Positve Case GET Per ID 
    [Documentation]    Test GET request to the API
    Create Session    Base    ${BASE_URL}
    ${headers}=    Create Dictionary    Content-Type    application/json
    ${response}=    GET On Session    Base    /api/users/1    headers=${headers}  data=${payload}
    
    Log    ${response.status_code}
    Log    ${response.json()}
    
    #Check Status 
    Should Be Equal As Strings    ${response.status_code}    200

    #Check Field 
    ${json_response}=    Set Variable    ${response.json()}
        
    Delete All Sessions

Method-POST-PositiveCase            #Positve Case Method POST 
    [Documentation]    Test POST request to the API
    Create Session    Base    ${BASE_URL}
    ${headers}=    Create Dictionary    Content-Type    application/json
    ${response}=    POST On Session    Base    /api/users    headers=${headers}  data=${payload}
    
    Log    ${response.status_code}
    Log    ${response.json()}
    
    #Check Status 
    Should Be Equal As Strings    ${response.status_code}    201

    #Check Field 
    ${json_response}=    Set Variable    ${response.json()}
        
    Delete All Sessions

Method-PUT-PositiveCase            #Positve Case Method PUT  
    [Documentation]    Test POST request to the API
    Create Session    Base    ${BASE_URL}
    ${headers}=    Create Dictionary    Content-Type    application/json
    ${response}=    PUT On Session    Base    /api/users/1    headers=${headers}  data=${payload}
    
    Log    ${response.status_code}
    Log    ${response.json()}
    
    #Check Status 
    Should Be Equal As Strings    ${response.status_code}    200

    #Check Field 
    ${json_response}=    Set Variable    ${response.json()}
    
    ${field_id}=         Set Variable    ${json_response['id']}  
    ${field_email}=      Set Variable    ${json_response['email']}  
    ${field_first}=      Set Variable    ${json_response['first_name']}  
    ${field_last}=       Set Variable    ${json_response['last_name']}  

    Should Be Equal As Strings    ${field_id}       ${EXPECTED_id}
    Should Be Equal As Strings    ${field_email}    ${EXPECTED_email}
    Should Be Equal As Strings    ${field_first}    ${EXPECTED_first_name} 
    Should Be Equal As Strings    ${field_last}     ${EXPECTED_last_name}
        
    Delete All Sessions


Method-POST-Case-Missing-Request-Body-Fields                #Negative Case 

    [Documentation]    Test POST request to the API
    Create Session    Base    ${BASE_URL}
    ${headers}=    Create Dictionary    Content-Type    application/json
    ${response}=    POST On Session    Base    /api/users    headers=${headers}  data=${payload2}
    
    Log    ${response.status_code}
    Log    ${response.json()}
    
    Should Be Equal As Strings    ${response.status_code}    201

    ${json_response}=    Set Variable    ${response.json()}
    ${field_id}=    Set Variable    ${json_response['id']}  
    ${field_email}=    Set Variable    ${json_response['email']}  
    ${field_first}=    Set Variable    ${json_response['first_name']}  
    ${field_last}=    Set Variable    ${json_response['last_name']}  

    Should Be Equal As Strings    ${field_id}    ${EXPECTED_id}
    Should Be Equal As Strings    ${field_email}    ${EXPECTED_email}
    Should Be Equal As Strings    ${field_first}    ${EXPECTED_first_name} 
    Should Be Equal As Strings    ${field_last}    ${EXPECTED_last_name}
    Delete All Sessions



Method-POST-Response-Not-Equals-with-Request                    #Negative Case 
    [Documentation]    Test POST request to the API
    Create Session    Base    ${BASE_URL}
    ${headers}=    Create Dictionary    Content-Type    application/json
    ${response}=    POST On Session    Base    /api/users    headers=${headers}  data=${payload4}
    
    Log    ${response.json()}
    
    ${json_response}=    Set Variable    ${response.json()}

    ${field_id}=         Set Variable    ${json_response['id']}  
    ${field_email}=      Set Variable    ${json_response['email']}  
    ${field_first}=      Set Variable    ${json_response['first_name']}  
    ${field_last}=       Set Variable    ${json_response['last_name']}  

    Should Be Equal As Strings    ${field_id}       ${EXPECTED_id}
    Should Be Equal As Strings    ${field_email}    ${EXPECTED_email}
    Should Be Equal As Strings    ${field_first}    ${EXPECTED_first_name} 
    Should Be Equal As Strings    ${field_last}     ${EXPECTED_last_name}
    Delete All Sessions
