file_name=open("double_shift.json","w")

whole_string = """{
    
  "title": "Double shift",
  "rules": [
    {
      "description": "Press key twice gives the shifted value.",
      "manipulators": [
          
          """
keycodes=['1','2','3','4','5','6','7','8','9','0','hyphen','equal_sign',\
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(keycodes)):  
    k=keycodes[i]
    whole_string+=""" 
    {
        "conditions": [
            {
                "name": \""""+k+""" pressed",
                "type": "variable_if",
                "value": 1
            }
        ],
        "from": {
            "key_code": \""""+k+"""",
            "modifiers": {
                "optional": [
                    "any"
                ]
            }
        },
        "to": [
            {
                "key_code": "delete_or_backspace",
                "modifiers": [
                    "left_shift"
                ]
            },
            {
                "key_code": \""""+k+"""",
                "modifiers": [
                    "left_shift"
                ]
            }
        ],
        "type": "basic"
    },
    {
        "from": {
            "key_code": \""""+k+"""",
            "modifiers": {
                "optional": [
                    "any"
                ]
            }
        },
        "to": [
            {
                "set_variable": {
                    "name": \""""+k+""" pressed",
                    "value": 1
                }
            },
                                  
          {
            "key_code": \""""+k+""""
          }
        ],
        "to_delayed_action": {
            "to_if_canceled": [
                {
                    "set_variable": {
                        "name": \""""+k+""" pressed",
                        "value": 0
                    }
                }
            ],
            "to_if_invoked": [
                {
                    "set_variable": {
                        "name": \""""+k+""" pressed",
                        "value": 0
                    }
                }
            ]
        },
        "type": "basic"
    }
    
    """
    if i!=len(keycodes)-1:
        whole_string+=","
        
whole_string+="""
      ]
    }
  ]
}
"""
file_name.write(whole_string)
