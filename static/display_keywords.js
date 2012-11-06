
function display_keywords(keywords, words_to_matches){
  kw_list = document.getElementById('kw_list');
  for (var i=0; i<keywords.length; i++){
    var keyword = keywords[i];
    var keyword_li = document.createElement('li');
    keyword_li.innerHTML = keyword;
    display_people(keyword_li, keyword, words_to_matches);
    kw_list.appendChild(keyword_li);
  };
};

function display_people(keyword_li, keyword, words_to_matches){
 var people_list = document.createElement('ul');
    keyword_li.appendChild(people_list);
    // console.log(keyword);
    // console.log(words_to_matches);
    var people = words_to_matches[keyword];
    for (var i=0; i<people.length; i++) {
      var person_li = document.createElement('li');
      person_li.innerHTML = people[i];
      people_list.appendChild(person_li);
    };
};

function display_matches() {
  var user_name = document.getElementById('name').value
  $.post('http://localhost:5000/', {fname: user_name}, function(data, textStatus){
    data = $.parseJSON(data);
    console.log(data);
    var keywords = data[0];
    var words_to_matches = data[1];
    display_keywords(keywords, words_to_matches);
  });
};

button = document.getElementById('button');
button.addEventListener('click', display_matches);

name_input = document.getElementById('name');
name_input.addEventListener('keypress', function(e){
  if (e.keyCode == 13) {
    console.log('Enter pressed')
    display_matches();
  }
});

