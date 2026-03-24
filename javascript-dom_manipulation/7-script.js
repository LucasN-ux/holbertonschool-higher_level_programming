async function getdata() {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        const moviesList = document.querySelector('#list_movies');
        result.results.forEach(movie => {
            const li = document.createElement('li');
            li.textContent = movie.title;
            moviesList.appendChild(li);
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}
getdata();
