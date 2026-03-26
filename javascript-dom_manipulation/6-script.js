async function getdata() {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        const character = document.querySelector('#character');
        character.textContent = result.name;
        } catch (error) {
        console.error('Error fetching data:', error);
    }
}
getdata();
