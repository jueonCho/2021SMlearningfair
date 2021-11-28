print("=====================================================================")
print("안녕하세요! 당신을 위한 맞춤 의류 추천 프로그램 2ig2ag입니다. 답변은 숫자로 입력하여 주시기 바랍니다.")
print("가을을 맞이하여, 가을에 대표적으로 입는 옷들을 추천해드리겠습니다!")
print()
#clothlist = (mu,md,wu,wd)
while True:
   cOne = None
   while cOne not in ['1', '2']:
      cOne = input("성별을 입력해주세요. (단, 남성이면 '1', 여성이면 '2'  중 선택가능합니다.) : ")
      if cOne == '1':
         print("선택한 성별 : 남성")   
      elif cOne == '2':
         print("선택한 성별 : 여성")
         
   cTwo = None
   while cTwo not in ['1', '2']:
      cTwo = input("상하의를 입력해주세요. (단, 상의면 '1', 하의면 '2' 중 선택가능합니다.) : ")
      if cTwo == '1':
         print("선택한 상하의 : 상의")
      elif cTwo == '2':
         print("선택한 상하의 : 하의")

   cThree = None
   # 남성, 상의   
   if cOne=='1' and cTwo=='1':
      while cThree not in ['1', '2', '3', '4']:
         cThree = input("원하는 종류를 입력해주세요. (단, 셔츠면 '1', 니트면 '2', 후드면 '3', 코트이면 '4' 중 선택 가능합니다.) : ")
         if cThree == '1':
            print("원하는 종류 : 셔츠")  
         elif cThree == '2':
            print("원하는 종류 : 니트")  
         elif cThree == '3':
            print("원하는 종류 : 후드")  
         elif cThree == '4':
            print("원하는 종류 : 코트")  
                                           
   # 남성, 하의             
   elif cOne=='1' and cTwo=='2':
      while cThree not in ['1', '2']:
         cThree = input("원하는 종류를 입력해주세요. (단, 청바지 '1', 슬랙스 '2' 중 선택 가능합니다.) : ")
         if cThree == '1':
            print("원하는 종류 : 청바지")    
         elif cThree == '2':
            print("원하는 종류 : 슬랙스")    
                         
   # 여성, 상의                
   elif cOne=='2' and cTwo=='1':
      while cThree not in ['1', '2', '3', '4']:
         cThree = input("원하는 종류를 입력해주세요. (단, 셔츠면 '1', 니트면 '2', 후드면 '3', 코트이면 '4' 중 선택 가능합니다.) : ")
         if cThree == '1':
            print("원하는 종류 : 셔츠")    
         elif cThree == '2':
            print("원하는 종류 : 니트")    
         elif cThree == '3':
            print("원하는 종류 : 후드")    
         elif cThree == '4':
            print("원하는 종류 : 코트")
            
   # 여성, 하의                
   elif cOne=='2' and cTwo=='2':
      while cThree not in ['1', '2', '3']:
         cThree = input("원하는 종류를 입력해주세요. (단, 청바지 '1', 슬랙스 '2', 치마 '3' 중 선택 가능합니다.) : ")
         if cThree == '1':
            print("원하는 종류 : 청바지") 
            ccThree = '청바지'
         elif cThree == '2':
            print("원하는 종류 : 슬랙스") 
            ccThree = '슬랙스'
         elif cThree == '3':
            print("원하는 종류 : 치마") 
            ccThree = '치마'
        
   print()
   f = open('%s_%s_%s.txt'%(cOne,cTwo,cThree), 'r',encoding='UTF8')
   data = f.read()
   print("추천하는 의류 사이트입니다.")
   print(data)
   f.close()

   print("더 찾으시는 상품이 있으시다면 네, 없다면 아니요를 입력해주세요.")
   four=input("대답: ")

   if four == "아니요":
      print("사용해주셔서 감사합니다. 즐거운 쇼핑되세요!")
      break

print("\n=====================================================================")
