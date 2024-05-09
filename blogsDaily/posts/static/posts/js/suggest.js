
const App =()=>{
    return (
        <div>
            <Container />
            <Input />
        </div>
    )
}

const Container =()=>{
    return (
        <div>hello</div>
    )
}

const Input = ()=>{
    return (
        <div>
            <input type='text' class="w-75 h-25 "></input>
            <button class='btn btn-success'>Search GPT</button>
        </div>
    )
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<App/>)



