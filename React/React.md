### React Element 
##### React Element Tags
- just like html tags

```
<h1>My Header</h1>
<button>My Button</button>
<ul>
	<li>list item 1</li>
	<li>list item 2</li>
	<li>list item 3</li>
</ul>
```

###### React Element Inline Styles
```
<h1 style={{ color: 'blue', textAlign: 'center' }}>This is a header</h1>
```

###### React Fragments
- React has a special element called a fragment. It’s a special element that doesn’t actually render into the DOM, but can act as a parent to a group of elements.

```
import { Fragment } from 'react'

<Fragment>
	<h1> My H1 </h1>
	<p> My Paragraph </p>
</Fragment>
```
You can also simply use:
```
<>
	<h1> My H1 </h1>
	<p> My Paragraph </p>
</>
```

### React Components

###### Functional Components
```
function MyComponent() {
  return <h1>My Component</h1>
}
```
Arrow functions = () =>
```
const MyComponent = () => {
    return <h1> My Componenet </h1>
}

const MyOtherComponent = () => {
	return (
		<div>
			<MyComponent />
			<p> Sample Text </p>
		</div>
	)
}
```
###### Component Props
We can pass data to our components through custom attributes on the component element. We can choose any name for the attribute as long they don’t overlap with the existing general element attributes (i.e. className, styles, onClick etc.). These properties are then grouped into an object where the attribute name is the key, and the value is the value. Here we are passing a prop title from the App component to our component MyComponent.
```
const MyComponent = (props) => {
	return <h1>{props.title}</h1>
}

const App = () => {
	return (
		<MyComponent title="Hello World" /> // Props == { title: "Hello World" }
	)
}
```

###### The Children Props
All component have a special prop called children. Any data (usually components and react elements) sitting between the opening and closing tags of the component get passed in as children.
```
const Greeting = ({ children }) => {
    return children // <h1> Hello World </h1>
}

const App = () => {
    return(
        <Greeting>
            <h1> Hello World </h1>
        </Greeting>
    )
}
```
###### Conditional Rendering
```
const Greeting = ({large}) => {
	if(large) {
		return <h1> Hello World! </h1>
	}
	return <p> Hello World! </p>
}

const App = () => {
	return (
		<div>
			<Greeting large={true}/> // <h1> Hello World! </h1>
			<Greeting large={false}/> // <p> Hello World! </p>
		</div>
	)
}
```
###### List in Componenets
- duplicate componenet or multiple componenets, we can do so by looping through an array with the .map() method as long as we return JSX from the callback.

```
const ShoppingList = ({items}) => {
	return (
		<ul>
			{items.map((item) => <li key={item}> {item} </li>)}
		</ul>
	)
}

const App = () => {
	const groceries = ['broccoli', 'carrots', 'chicken', 'garlic'];
	return <ShoppingList items={groceries} />
}
```

