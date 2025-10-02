import "./App.css"
import TextDisplayComponent from "./components/TextDisplayComponent"

function App() {

    return (

        <div
            className="app-container"
        >
            <header
                className="app-header"
            >
                <h1>
                    Japanese Learning Chat Bot
                </h1>
            </header>

            <main>
                <TextDisplayComponent />
            </main>
        </div>
    )
}

export default App