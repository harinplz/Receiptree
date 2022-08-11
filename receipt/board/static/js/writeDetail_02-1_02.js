
'use strict';



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
      //addNewComment();
    } else {
      alert('댓글이 입력되지 않았습니다 😳');
    }
  })
}


postCommentInFeed();
