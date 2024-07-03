// Firebase configuration
const firebaseConfig = require('serviceAccountKey.json');

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Reference to the "students" node in the database
const studentsRef = firebase.database().ref('students');

// Function to fetch and display student information
function displayStudentInfo() {
    studentsRef.on('value', (snapshot) => {
        const studentInfoContainer = document.getElementById('studentInfo');
        studentInfoContainer.innerHTML = ''; // Clear previous content

        snapshot.forEach((childSnapshot) => {
            const studentId = childSnapshot.key;
            const studentData = childSnapshot.val();

            // Create a card for each student
            const studentCard = document.createElement('div');
            studentCard.classList.add('studentCard');
            
            studentCard.innerHTML = `
                <h2>${studentData.name}</h2>
                <p>Student ID: ${studentId}</p>
                <p>Major: ${studentData.major}</p>
                <p>Starting Year: ${studentData.starting_year}</p>
                <p>Total Attendance: ${studentData.total_attendance}</p>
                <p>Standing: ${studentData.standing}</p>
                <p>Year: ${studentData.year}</p>
                <p>Last Attendance Time: ${studentData.last_attendance_time}</p>
            `;

            studentInfoContainer.appendChild(studentCard);
        });
    });
}

// Initial display
displayStudentInfo();
 
