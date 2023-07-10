const inputElement = document.getElementById('university-input');
const datalist = document.getElementById('suggestions');

window.onload = function () {
  inputElement.addEventListener("mouseenter", function () {
    fetchData(inputElement);
  });
}

function fetchData(input) {
  // Obtenemos el valor del input
  const searchTerm = input.value;

  // Obtenemos los datos del JSON
  fetch('../assets/json/universities.json')
    .then(response => response.json())
    .then(data => {
      // Filtramos los datos para obtener los que coinciden con el término de búsqueda
      const filteredData = Object.values(data).filter(university => {
        return university.name.toLowerCase().includes(searchTerm.toLowerCase());
      });

      // Creamos la lista desplegable con los resultados
      const dropdown = document.createElement('div');
      dropdown.classList.add('dropdown');

      filteredData.forEach(university => {
        const option = document.createElement('div');
        option.classList.add('dropdown-option');
        option.textContent = `${university.name}, ${university.country}`;
        dropdown.appendChild(option);
      });

      // Vinculamos el datalist al input y mostramos la lista desplegable
      input.setAttribute('list', 'suggestions');
      datalist.innerHTML = '';
      datalist.appendChild(dropdown);

      // Eliminamos la lista desplegable si el valor del input está vacío
      if (searchTerm === '') {
        datalist.innerHTML = '';
      }
    })
    .catch(error => console.error(error));
}
