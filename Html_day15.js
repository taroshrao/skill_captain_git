// Task 1: Create a Simple JSX Component//

  import React from 'react';
    
    function Welcome() {
      const name = "Tarosh";
      return <h1>Hello, {name}!</h1>;
    }
    
    export default Welcome;

//Task 2: Build a Reusable Component//
    // Create a UserCard.js component that takes name and age as props in the src folder //
    
    import React from 'react';
export default function UserCard({ name, age }) {
  return (
    <div>
      <h2>{name}</h2>
      <p>Age: {age}</p>
    </div>
  );
}

    //Create UserCard.js in the src folder//
    import React from 'react';
import Welcome from './Welcome';
import UserCard from './UserCard';

export default function App() {
  return (
    <div className="App">
      <Welcome />
      <UserCard name="Tarosh" age={28} />
      <UserCard name="Megha" age={34} />
    </div>
  );
}

//Task 3: Dynamic List with JSX//
import React from 'react';
import Welcome from './Welcome';
import UserCard from './UserCard';

function App() {
  const users = [
    { id: 1, name: 'Alice', age: 28 },
    { id: 2, name: 'Bob', age: 34 },
    { id: 3, name: 'Charlie', age: 22 }
  ];

  return (
    <div className="App">
      <Welcome />
      {users.map(user => (
        <UserCard key={user.id} name={user.name} age={user.age} />
      ))}
    </div>
  );
}

export default App;




