function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function deleteImage(id){
//  put here a validation message
  let res = confirm("Estas seguro?...");
//  console.log(res)
  if (res & id != ''){
    fetch('/gallery/delete_image/', {
      method: 'POST',
      credentials: 'same-origin',
      headers:{
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
          'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify({image_id: id}) //JavaScript object of data to POST
    })
    .then(response => {
        return response.json() //Convert response to JSON
    })
    .then(data => {
    //Perform actions with the response data from the view
    console.log(data);
    window.location.reload(false);
    })
  }else {
    console.log('Cancelado..')
  }
}