### React Hooks
1. The mounting phase when a component is created and inserted into the DOM. This is the initial render and only happens once in a components lifecycle.
2. The updating phase is when a component re-renders due to updates. This happens either due to prop changes or state changes (more below).
3. The final phase is the un-mounting phase, when a component is removed from the DOM.

###### useState
useState hook allows us to store values scoped to a component. Any changes to those values will cause the component and any of it’s child components to re-render.

###### Example
```
import { useState } from 'react';

const Counter = () => {
	const [count, setCount] = useState(0);
	const increment = () => setCount(count + 1);
	const decrement = () => setCount(count - 1);

	return (
		<div>
			{count}
			<button onClick={increment}> increment </button>
			<button onClick={decrement}> decrement </button>
		</div>
	)
}
```

###### useEffect
useEffect is a hook that allows us to create side effects in our functional components.

```
import { useState, useEffect } from 'react'

const UserList = () => {
	const [userList, setUserList] = useState([]);

	useEffect(() => {
		fetch('https://jsonplaceholder.typicode.com/users')
		.then(response => response.json())
		.then(users => setUserList(users))
	}, []);

	return (
		<div>
			{ userList.map(user => <h2 key={user.id}> {user.name} </h2>) }
		</div>
	)
}
```

###### useLayoutEffect
The useLayoutEffect hook is almost identical to the useEffect hook except it runs the effect callback immediately after DOM changes.

```
import { useLayoutEffect } from 'react'

const MyComponent = () => {
	useLayoutEffect(() => {
		// side effect code here
	}, [// dependencies go here]);
}
```


###### useRef
useRef is a hook that stores a value in a component like useState except changes to that value won’t cause the component to re-render.
```
import { useRef } from 'react';

export default function Counter() {
  let ref = useRef(0);

  function handleClick() {
    ref.current = ref.current + 1;
  }

  return (
    <>
	    <h1>count: {ref.current} </h1>
	    <button onClick={handleClick}>
	      Click me!
	    </button>
    </>
  );
}
```
