
const main = () => {

  let cookies = document.getElementById("cookies");
  let outputContent = document.getElementById("outputContent");

  document.getElementById("showCookies").addEventListener("click", () => {
    show("cookies");
  })
  cookies.appendChild(paste.cookies());

  let user_agent = document.getElementById("user-agent");
  document.getElementById("showUserAgent").addEventListener("click",() => {
    show("user-agent");
  })
  user_agent.appendChild(paste.userAgent());

  let location = document.getElementById("location");
  document.getElementById("showLocation").addEventListener("click", () => {
    show("location");
  })
  paste.location()
}

const show = (id) => {

  // console.log(`1: ${id}`);

  let element = document.getElementById(id);
  let content = document.getElementById("outputContent");

  content = content.children;

  for (let i=0; i<content.length;i++) {
    if (content[i].id != id ) {
      content[i].style.display = "none"
    }
  }

  console.log(`2: ${element.value}`)
  element.style.display = "block";
}


const locationBreak = () => {
  document.getElementById("location").appendChild(document.createElement("hr"))
}

const paste = {

  cookies: () => {
      let cookies = document.cookie
      let table = document.createElement("table");
      let tableHead = document.createElement("thead");
      let tableBody = document.createElement("tbody");
      let headerRow = document.createElement("tr");
      let tableHeader1 = document.createElement("th");
      let tableHeader2 = document.createElement("th");
      let tableHeaderText1 = document.createTextNode("Name");
      let tableHeaderText2 = document.createTextNode("Value");

      tableHeader1.appendChild(tableHeaderText1);
      tableHeader2.appendChild(tableHeaderText2);
      headerRow.appendChild(tableHeader1);
      headerRow.appendChild(tableHeader2);
      tableHead.appendChild(headerRow);
      table.appendChild(headerRow);

      cookies.split(";").forEach(cookie => {
        let scookie = cookie.split("=")
        // console.log(`Split: ${scookie}`)
        let tableRow = document.createElement("tr");
        let data1 = document.createElement("td");
        let data2 = document.createElement("td");
        let dataText1 = document.createTextNode(scookie[0]);
        let dataText2 = document.createTextNode(scookie[1]);
        data1.appendChild(dataText1);
        data2.appendChild(dataText2);
        tableRow.appendChild(data1);
        tableRow.appendChild(data2);
        tableBody.appendChild(tableRow);
      });
      table.appendChild(tableBody);
      return table

    },

  userAgent: () => {
      let userAgent = document.createElement("span");
      userAgent.innerText = navigator.userAgent;
      return userAgent;
    },

  location: async () => {

    let re = /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/
    let mainBoxEl = document.createElement("div");

    let ipaddress = await fetch("https://www.cloudflare.com/cdn-cgi/trace")
    .then(response => response.text())
    .then(data => data.match(re)[0])
    .catch( error => {
      return console.error(error);
    })

     return await fetch(`http://ip-api.com/json/${ipaddress}`)
    .then(response => response.json())
    .then(data => {
      let mapBoxEl = document.createElement("div");
      let infoBoxEl = document.createElement("div");
      let br = document.createElement("br");
      let countryEl = document.createElement("div");
      let countryCodeEl = document.createElement("div");

      let regionEl = document.createElement("div");
      let regionNameEl = document.createElement("div");

      let cityEl = document.createElement("div");
      let zipEl = document.createElement("div");

      let latLonEl = document.createElement("div");
      let timezoneEl = document.createElement("div");

      let ispEl = document.createElement("div");
      let orgEl = document.createElement("div");
      let ipEl = document.createElement("div");

      let mapEl = document.createElement("a");

      infoBoxEl.appendChild(ipEl.appendChild(document.createTextNode(`\n\nInternet Protocol Address (IP): ${data.query}\n\n`)));
      infoBoxEl.appendChild(orgEl.appendChild(document.createTextNode(`Orginization ID: ${data.org}\n\n`)));
      infoBoxEl.appendChild(ispEl.appendChild(document.createTextNode(`Internet Service Provider (ISP): ${data.isp}\n\n`)));
      infoBoxEl.appendChild(countryEl.appendChild(document.createTextNode(`Country: ${data.country}\n\n`)));
      infoBoxEl.appendChild(countryCodeEl.appendChild(document.createTextNode(`Country Code: ${data.countryCode}\n\n`)));
      infoBoxEl.appendChild(regionEl.appendChild(document.createTextNode(`Region: ${data.region}\n\n`)));
      infoBoxEl.appendChild(regionNameEl.appendChild(document.createTextNode(`Region Name: ${data.regionName}\n\n`)));
      infoBoxEl.appendChild(cityEl.appendChild(document.createTextNode(`City: ${data.city}\n\n`)));
      infoBoxEl.appendChild(zipEl.appendChild(document.createTextNode(`Zip Code: ${data.zip}\n\n`)));
      infoBoxEl.appendChild(latLonEl.appendChild(document.createTextNode(`Longitude/Latitude: ${data.lat}, ${data.lon}\n\n`)));
      infoBoxEl.appendChild(timezoneEl.appendChild(document.createTextNode(`Time Zone: ${data.timezone}\n\n`)));

      mapEl.setAttribute("href", `https://www.openstreetmap.org/#map=12/${data.lat}/${data.lon}`);
      mapEl.setAttribute("target", "_blank")
      mapEl.innerText = "See on map.";
      mapBoxEl.appendChild(mapEl);
      mainBoxEl.appendChild(mapBoxEl);
      mainBoxEl.appendChild(infoBoxEl);
      document.getElementById("location").appendChild(mainBoxEl);
    })
    .catch( error => {
      return console.error(error);
    })

    },

}
main()


/*
  @cookies
  descrpiton
  user
  updsated:
*/
// cookies: () => {
//     let cookies = document.cookie
//     let table = document.createElement("table");
//     let tableHead = document.createElement("thead");
//     let tableBody = document.createElement("tbody");
//     let headerRow = document.createElement("tr");
//     let tableHeader1 = document.createElement("th");
//     let tableHeader2 = document.createElement("th");
//     let tableHeaderText1 = document.createTextNode("Name");
//     let tableHeaderText2 = document.createTextNode("Value");
//
//     tableHeader1.appendChild(tableHeaderText1);
//     tableHeader2.appendChild(tableHeaderText2);
//     headerRow.appendChild(tableHeader1);
//     headerRow.appendChild(tableHeader2);
//     tableHead.appendChild(headerRow);
//     table.appendChild(headerRow);
//
//     cookies.split(";").forEach(cookie => {
//       let scookie = cookie.split("=")
//       console.log(`Split: ${scookie}`)
//       let tableRow = document.createElement("tr");
//       let data1 = document.createElement("td");
//       let data2 = document.createElement("td");
//       let dataText1 = document.createTextNode(scookie[0]);
//       let dataText2 = document.createTextNode(scookie[1]);
//       data1.appendChild(dataText1);
//       data2.appendChild(dataText2);
//       tableRow.appendChild(data1);
//       tableRow.appendChild(data2);
//       tableBody.appendChild(tableRow);
//     });
//     table.appendChild(tableBody);
//     return table
//
//   },
