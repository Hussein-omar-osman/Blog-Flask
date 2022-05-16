const btnJoke = document.getElementById('joke');
const p2 = document.getElementById('quote');
const p3 = document.getElementById('author');
const newsTitle = document.querySelectorAll('.blog-title');
const newsDes = document.querySelectorAll('.blog-content');

btnJoke.addEventListener('click', () => {
  getData();
});

async function getData() {
  let res = await fetch('http://quotes.stormconsultancy.co.uk/random.json');
  let data = await res.json();
  if (data) {
    console.log(data);
    p2.innerText = data.quote;
    p3.innerText = `- ${data.author} -`;
    return data;
  } else {
    console.log('no data');
  }
}

for (nt of newsTitle) {
  titleContent = nt.textContent;

  len = nt.textContent.length;
  if (len > 8) {
    content_dis = titleContent.slice(0, 8);
    nt.innerText = `${content_dis}...`;
  }
}

for (nt of newsDes) {
  DesContent = nt.textContent;
  console.log(DesContent);
  len = DesContent.length;
  console.log(len);
  if (len > 180) {
    content_dis = DesContent.slice(0, 180);
    nt.innerText = `${content_dis}...`;
    console.log(DesContent);
  }
  console.log(DesContent);
}
