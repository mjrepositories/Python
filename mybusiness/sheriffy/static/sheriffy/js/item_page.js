let con = document.getElementById('footer')

const modals = document.querySelectorAll('.myModal')

const images = document.querySelectorAll('.myImg')

const modal_images = document.querySelectorAll('.img')

const spans = document.querySelectorAll('.span')

const modals_counter = document.querySelectorAll('.myModal').length - 1

for (let i = 0; i <= modals_counter; ++i) {


    // Get the modal
    var modal = document.getElementsByClassName("myModal")[i];

    modal.onclick = function(){
    modal.style.display = "none";
    }

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    var img = document.getElementsByClassName("myImg")[i];
    var modalImg = document.getElementsByClassName("img")[i];
    img.onclick = function(){
      modal.style.display = "block";
      modalImg.src = this.src;

    }


    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[i];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
      modal.style.display = "none";
    }

}

function alerting(){
alert('Element clicked through function!')
}




