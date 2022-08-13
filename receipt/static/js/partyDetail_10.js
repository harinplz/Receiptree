
'use strict';

// 클릭하여 파티원별 영수증 보기

function openMenu(pageName, elmnt) {
    // Hide all elements with class="tabcontent" by default */
    var i, content, tab;
    content = document.getElementsByClassName("receipt");
    for (i = 0; i < content.length; i++) {
        content[i].style.display = "none";
    }
  
    // Remove the background color of all tablinks/buttons
    tab = document.getElementsByClassName("user_photo");
    for (i = 0; i < tab.length; i++) {  
        tab[i].style.border = "";
        

    }

    

    // Show the specific tab content
    document.getElementById(pageName).style.display = "block";
    
  
    // Add the specific color to the button used to open the tab content
    elmnt.style.border="10px solid #1824BF"
    
  }
  
  // Get the element with id="defaultOpen" and click on it
  document.getElementById("defaultOpen").click();
  








  
//댓글

const postCommentInFeed = () => {
  const commentInput = document.getElementById('comment_textarea');
  const commentPostBtn = document.getElementsByClassName('comment_btn')[0];

  // 댓글 입력시 요소 생성
  const addNewComment = () => {
    const newCommentLocation = document.getElementsByClassName('comment_list')[0];
    const newComment = document.createElement('li');

    newComment.innerHTML = 
    `
    <div class="d-flex">
      <div class="comment_profile"><img class="rounded-circle" src="https://dummyimage.com/50x50/ced4da/6c757d.jpg" alt="..." /></div>
      <div class="comment_area">
          <div class="commentsName">작성자NAME</div>
          <div class="commentsContent">${commentInput.value}</div>                      
      </div>
  </div>
  `;
    
    

    newCommentLocation.appendChild(newComment);
    commentInput.value = '';
  }


  // 사용자 입력 들어올 시, 게시 버튼 활성화

  // 댓글 게시
  commentPostBtn.addEventListener('click', () => {
    if (commentInput.value) {
      addNewComment();
    } else {
      alert('댓글이 입력되지 않았습니다 😳');
    }
  })
}


postCommentInFeed();