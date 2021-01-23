var getUrl = window.location;
var baseUrl = getUrl.protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[0];

function load_json(username) {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", baseUrl + "api/v1/links/?format=json&username=" + username);

  xhr.addEventListener("load", function () {
    var response = xhr.responseText;
    var products = JSON.parse(response);
    var size = Object.keys(products).length;

    function* range(start, end) {
      for (let i = start; i <= end; i++) {
        yield i;
      }
    }
    var content_fim = '';

    for (i of range(0, size - 1)) {

      title_url = products[i]['title'];
      url_val = products[i]['url'];
      id_val = products[i]['id'];

      background_color = products[i]["background_color"];

      content = `  <a href="redirect/${id_val}/" >

              <div style="background-color: ${background_color}">
                <h3>${title_url}</h3>
                </div>
                </a>
                `
      content_fim = content_fim + content;
    };
    document.getElementById("content_user").innerHTML = content_fim;


  });

  xhr.send();
};

const username = document.getElementById("user_name").innerHTML;

load_json(username.slice(1));









