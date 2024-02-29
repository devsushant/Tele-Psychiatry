const toggleButtons = document.querySelectorAll('.toggle-button');

  toggleButtons.forEach(button => {
    button.addEventListener('click', function() {
      const answer = this.parentNode.nextElementSibling;
      const isOpen = answer.style.display === 'block';

      if (isOpen) {
        answer.style.maxHeight = '0';
        setTimeout(() => {
          answer.style.display = 'none';
        }, 300); // Same duration as transition in CSS
        this.classList.remove('fa-minus');
        this.classList.add('fa-plus');
      } else {
        answer.style.display = 'block';
        const answerHeight = answer.scrollHeight + 'px';
        answer.style.maxHeight = answerHeight;
        this.classList.remove('fa-plus');
        this.classList.add('fa-minus');
      }
    });
  });

// Smooth Scrolling
$('#navbar a, .btn').on('click', function(event) {
  if (this.hash !== '') {
    event.preventDefault();

    const hash = this.hash;

    $('html, body').animate(
      {
        scrollTop: $(hash).offset().top - 100
      },
      800
    );
  }
});


$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})


function validateForm() {
  var name = document.getElementById("name").value;
  var phone = document.getElementById("phone").value;
  var address = document.getElementById("address").value;
  var current_password = document.getElementById("current_password").value;
  var new_password = document.getElementById("new_password").value;
  var confirm_new_password = document.getElementById("confirm_new_password").value;

  if (name == "" || phone == "" || address == "" || current_password == "" || new_password == "" || confirm_new_password == "") {
    alert("All fields must be filled out");
    return false;
  }

  if (new_password != confirm_new_password) {
    alert("New Passwords do not match");
    return false;
  }

  return true;
}