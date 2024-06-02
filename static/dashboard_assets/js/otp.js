const form = document.querySelector("#otp-form");
const inputs = document.querySelectorAll(".otp-input");
const verifyBtn = document.querySelector("#verify-btn");

const isAllInputFilled = () => {
  return Array.from(inputs).every((item) => item.value);
};

const getOtpText = () => {
  let text = "";
  inputs.forEach((input) => {
    text += input.value;
  });
  return text;
};


const toggleFilledClass = (field) => {
  if (field.value) {
    field.classList.add("filled");
  } else {
    field.classList.remove("filled");
  }
};

form.addEventListener("input", (e) => {
  const target = e.target;
  const value = target.value;
  console.log({ target, value });
  toggleFilledClass(target);
  if (target.nextElementSibling) {
    target.nextElementSibling.focus();
  }
  verifyOTP();
});

inputs.forEach((input, currentIndex) => {
  // fill check
  toggleFilledClass(input);

  // paste event
  input.addEventListener("paste", (e) => {
    e.preventDefault();
    const text = e.clipboardData.getData("text");
    console.log(text);
    inputs.forEach((item, index) => {
      if (index >= currentIndex && text[index - currentIndex]) {
        item.focus();
        item.value = text[index - currentIndex] || "";
        toggleFilledClass(item);
        verifyOTP();
      }
    });
  });

  // backspace event
  input.addEventListener("keydown", (e) => {
    if (e.keyCode === 8) {
      e.preventDefault();
      input.value = "";
      // console.log(input.value);
      toggleFilledClass(input);
      if (input.previousElementSibling) {
        input.previousElementSibling.focus();
      }
    } else {
      if (input.value && input.nextElementSibling) {
        input.nextElementSibling.focus();
      }
    }
  });
});





// function validateMobile(){
//     let literal = {
//           req1: { selector: $("#phone_number"), regex: {value: /^[6-9]\d{9}$/, message: 'Please enter a valid mobile number'} }
//       }

//     var result = $.validate.rules(literal)
//     if(!result) return false
//     return true
//   }

function sendOTP(){
    const mobile = $("#phone_number").val()
    if (!validateMobile(mobile)) {
        show_error('Invalid mobile number');
        return;
    }
    let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
      url: '/auth/send_otp/',
      method: 'POST',
      data: {'mobile': mobile,'csrfmiddlewaretoken': csrfmiddlewaretoken},
      success: function(response){
        userId = response['user_id']
        window.location.href = "/verify_otp/";
        
      },
      error: function(response){
        show_error(response.responseJSON['error'])
      }
    })
  }


  function validateMobile(mobile) {
    const mobilePattern = /^[0-9]{10}$/;
    return mobilePattern.test(mobile);
}

function show_error(message) {
    alert(message);
}
 

verifyBtn.addEventListener("click", () => {
    const entered_otp = getOtpText();
    let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

    if(entered_otp.length < 4){
      show_success('Please enter a valid otp',classType='warning')
      return;
    }
    
    $.ajax({
      url: '/auth/verify_otp/',
      method: 'POST',
      data: {'otp': entered_otp,'csrfmiddlewaretoken': csrfmiddlewaretoken},
      success: function(response){
        window.location = response['path']
      },
      error: function(response){
        show_error(response.responseJSON['error'])
      }
    })
});


