# innerHTML, innerText, textContent의 차이점
- 예시 코드
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <div class="outer">
      나는 보입니당
      <span class="inner" style="display: none">나는 display 속성값이 none이라 안보여용</span>
    </div>

    <script>
      const outer = document.querySelector('.outer')
      console.log(outer.innerHTML)
      console.log(outer.innerText)
      console.log(outer.textContent)
    </script>
  </body>
</html>
```


## innerHTML
- innerHTML은 'Element'의 속성으로, **해당 Element내에 포함 된 HTML, XML을 가져오거나, 설정**할 수 있습니다.
- 위에서 innerHTML을 consol.log하면 **div안에 있는 HTML 전체 내용**을 가져오는 것을 확인 할 수 있습니다.
- console.log(outer.innerHTML)
  ```
  나는 보입니당
  <span class="inner" style="display: none">나는 display 속성값이 none이라 안보여용</span>
  ```

## innerText
- innerText는 'Element'의 속성으로, 해당 Element 내에서 **사용자에게 '보여지는' 텍스트 값**을 읽어옵니다.
- 위에서 innerText을 consol.log하면 **div 안에 숨겨진 요소의 텍스트는 반환하지 않습니다.**
- console.log(outer.innerText)
  ```
  나는 보입니당
  ```

## textContent
- textContent는 'Node'의 속성으로,innetText와는 달리 **script나 style태그와 상관없이 해상 노드와 자손의 텍스트 값**을 모두 읽어옵니다.
- 위에서 textContent을 consol.log하면 **div안에 텍스트 값을 모두 읽어옵니다.**
- console.log(outer.textContent)
  ```
  나는 보입니당
  나는 display 속성값이 none이라 안보여용
  ```
<br>
<br>

~~벌칙으로 만든 자바스크립트 정리 총총...~~
