import os

def banner():
    return '''                     ...:=-                   
                  .@@@@@@@@@@:                
                 #@@@@@@@@@@@@-               
                -=#%@@@@@@@@@@@               
                =-+#***@=%@@@@@:              
               :-=+-+:=**%#%@%*=              
               :-:=-=%%%%+=*@++.              
                ::.=*%%%#=+-+*=               
                 =#****%**+=##                
                ..+%%#%%%%%%@+:               
            ..--::.*%%%#*%%@*+++*+-.          
        :==----::-. :#%###+-.-++*******-      
      :=------:---:...-*=---:--:--=++****-    
      -:------:---.-==-=====:----------+=*    
     .-:-------:--:========---::-------:-*.   
     :-:----------:========------------:-*.   
     ..:----------:========-----------..=*    
     .:.:----------:=======----------- -.+    
     .-.:----------:======:--=-------:::.=    
     :-::------------====-.-==-------:- -=    
     -:::-----:--:-=:====.:-=:-==-----.:-=:   
     --.:-----:--:-=====-.:=-:-==----..--+:   
     --. ------.-:-=====:.--.:====---.--=*.   
'''


shot = 4
score = 100
os.system('clear')
def score_shot():
    return f'''{banner()}
Welcome to this game!
You have {shot} tries of shot
You have a Score of {score}
[1] Shot = 10
[2] Miss = -20
[3] Change tries
'''

print(score_shot())
while shot > 0:
    shot -= 1
    value = int(input("Value: "))
    if value == 1:
        score += 10
        os.system('clear')
        print(f'''{score_shot()}\n\n+10\n
+—————————————————————————+
| You have a Score of {score} |
+—————————————————————————+
''')
    elif value == 2:    
        score -= 20
        os.system('clear')
        print(f'''{score_shot()}\n\n-20\n
+—————————————————————————+
| You have a Score of {score}  |
+—————————————————————————+
        ''')
    elif value == 3:
        shot = int(input("how many tries : "))
        os.system('clear')
        print(f'{score_shot()}')
    else:
        print('invalid!\n')    
print("Final Score: ", score)