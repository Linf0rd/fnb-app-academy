document.getElementById("refresh")?.addEventListener("click", fetchContacts);
document.getElementById("addContact")?.addEventListener("click", addContact);

function fetchContacts() {
  fetch(rootPath + "controller/get-contacts/")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      displayOutput(data);
      //    console.log(data)
    });
}

function displayOutput(data) {
  output = "<table>";

  for (a in data) {
    output += `
            <tr onClick="editContact(${data[a].id})" class="individualContact">
              <td>
                <img src="${rootPath}controller/uploads/${data[a].avatar}" width="80"/>
              </td>
              <td><h5>${data[a].firstname}</h5></td>
              <td><h5>${data[a].lastname}</h5></td>
            </tr>
        `;
  }
  output += "</table>";
  document.getElementById("table").innerHTML = output;
}

function addContact() {
  window.open("add-contact.html", "_self");
}

function editContact(id) {
  window.open("edit-contact.html?id=" + id, "_self");
}

/// Submit Form

document.getElementById("submitForm")?.addEventListener("click", submitForm);
document.getElementById("homeLink")?.addEventListener("click", homeLink);

function submitForm(e) {
  e.preventDefault();

  const form = new FormData(document.querySelector("#editForm"));
  form.append("apiKey", apiKey);

  fetch(rootPath + "controller/insert-contact/", {
    method: "POST",
    headers: { Accept: "application/json, *.*" },
    body: form,
  })
    .then(function (response) {
      return response.text();
    })
    .then(function (data) {
      if (data == "1") {
        alert("Contact added");
        // link to home page
        homeLink();
      } else {
        alert(data);
        // link to home page
        homeLink();
      }
    });
}

function homeLink() {
  window.open("index.html", "_self");
}
