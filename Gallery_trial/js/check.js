
let images=document.querySelectorAll(".gallery")
let latestImageOpened;
let windowWidth=window.innerWidth;

if(images){
  images.forEach(function(image,index){
    image.onclick = function(){

      let getElementCss = window.getComputedStyle(image);

      let fullImageUrl = getElementCss.getPropertyValue("background-image");
      let newImgName= ((fullImageUrl.split("/Gallery/"))[1]).replace('")','')

      latestImageOpened=index+1;

      let container = document.body;
      let newImgWindow=document.createElement("div");
      container.appendChild(newImgWindow);
      newImgWindow.setAttribute("class","img-window");
      newImgWindow.setAttribute("onclick","closeImg()");

      let newImg=document.createElement("img");
      newImgWindow.appendChild(newImg)
      newImg.setAttribute("src",newImgName);
      newImg.setAttribute("id","current-img");

      newImg.onload = function(){

      let newPrevButton= document.createElement("a");
      let btnPrevText = document.createTextNode("Prev");
      newPrevButton.appendChild(btnPrevText);
      container.appendChild(newPrevButton);
      newPrevButton.setAttribute("class","img-btn-prev");
      newPrevButton.setAttribute("onclick","changeImg()");

      let newNextButton= document.createElement("a");
      let btnNextText = document.createTextNode("Next");
      newNextButton.appendChild(btnNextText);
      container.appendChild(newNextButton);
      newNextButton.setAttribute("class","img-btn-next");
      newNextButton.setAttribute("onclick","changeImg()");
    }
    }
  });
}

function closeImg(){
  alert("close")
  document.querySelector(".img-window").remove();
  document.querySelector(".img-btn-next").remove();
  document.querySelector(".img-btn-prev").remove();
}

function changeImg(changeDir){
  document.querySelector("#current-img").remove();
  let getImgWindow = document.querySelector(".img-window");
  let newImage = document.createElement("img");
  getImgWindow.appendChild(newImage);
if(changeDir === 1){
  let calcNewImg = latestImageOpened +1;
if(calcNewImg > images.length){
  calcNewImg = 1;
}}else if(changeDir === 0){
  let calcNewImg = latestImageOpened -1;
if(calcNewImg < images.length){
  calcNewImg = images.length;
}}
    newImage.setAttribute("src","img/img"+calcNewImg +".jpg");
  newImage.setAttribute("id","current-img");
  latestImageOpened = calcNewImg;

}
