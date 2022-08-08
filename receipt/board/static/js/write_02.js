
//지출 추가
function addRow() {
    // table element 찾기
    const table = document.getElementById('receipt-table');
    
    // 새 행(Row) 추가
    const newRow = table.insertRow();
    
    // 새 행(Row)에 Cell 추가
    const newCell1 = newRow.insertCell(0);
    const newCell2 = newRow.insertCell(1);
    const newCell3 = newRow.insertCell(2);
    const newCell4 = newRow.insertCell(3);
    
    // Cell에 텍스트 추가
    newCell1.innerHTML = "<input type='text' class='input-receipt1' placeholder='지출일시 입력'>";
    newCell2.innerHTML = "<input type='text' class='input-receipt2' placeholder='금액 입력'>";
    newCell3.innerHTML = "<textarea  class='input-receipt3' placeholder='사용처 입력'></textarea>";
    newCell4.innerHTML = "<textarea  class='input-receipt4' placeholder='내용 입력'></textarea><button class='delete'><img src='./image/delete.png'></button>";
  
    //금액합산
    $('.input-receipt2').blur(function () {
        var seip = 0;
        
        $('.input-receipt2').each(function(){ //클래스가 input-receipt2인 항목의 갯수만큼 진행
            seip += Number($(this).val()); 
        });
        
        //합계를 출력
        $("#use_sum").val(seip); 
    });

   
}

//금액 삭제
 $("#receipt-table").on("click", ".delete", function () {
         $(this).parent().parent().remove();
         var seip = 0;
        //삭제 후 다시 계산
         $('.input-receipt2').each(function(){ 
             seip += Number($(this).val()); 
         });
         
         //합계를 출력
         $("#use_sum").val(seip); 
         });










//합계
// function calcSum() {
//     // table element 찾기
//     const table = document.getElementById('input-receipt2');
    
//     // 합계 계산
//     let sum = 0;
//     for(let i = 0; i < table.rows.length; i++)  {
//       sum += parseInt(table.rows[i].cells[1].innerHTML);
//     }
    
//     // 합계 출력
//     document.getElementById('use_sum').innerText = sum;
    
//   }






