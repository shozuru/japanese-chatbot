import React, { useState, useEffect, useRef } from "react"
import axios from 'axios'
import "./TextDisplayComponent.css"

enum Sender {
    USER,
    SERVER
}

enum Intent {
    VOCAB = "vocab_practice",
    GRAMMAR = "grammar_practice",
    CHAT = "conversation_practice",
    HELP = "help",
    TRANSLATION = "translation"
}

interface ChatMessage {
    from: Sender
    message: string
}

const TextDisplayComponent: React.FC = () => {

    const [inputText, setInputText] = useState<string>('')
    const [responseText, setResponseText] = useState<string>('')
    const [chatMessageList, setChatMessageList] = useState<ChatMessage[]>([])
    const [currentVocabWord, setCurrentVocabWord] = useState<string>('')
    const [intent, setIntent] = useState<string>('')

    const bottomRef = useRef<HTMLDivElement | null>(null)

    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: "smooth" })
    }, [chatMessageList])

    const handleInput = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        e.preventDefault()
        setInputText(e.target.value)
    }

    const handleSubmitButton = (e: React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault()
        if (inputText.trim()) {

            const newUserMessage: ChatMessage = {
                from: Sender.USER,
                message: inputText.trim()
            }

            setChatMessageList(prev => [...prev, newUserMessage])
            handleSendTobackend(inputText.trim())
            setInputText('')
        }
    }

    const handleSendTobackend = async (inputText: string) => {
        if (intent === Intent.GRAMMAR) {
            axios.post('http://127.0.0.1:8000/grammar',
                {
                    message: inputText
                }
            )
                .then(res => {
                    setResponseText(res.data.response)
                })

            setIntent('')

        } else if (intent === Intent.CHAT && inputText == 'STOP') {
            axios.post('http://127.0.0.1:8000/stopConvo')
                .then(res => {
                    setResponseText(res.data.response)
                    setIntent('')
                })

        } else if (intent === Intent.CHAT) {
            axios.post('http://127.0.0.1:8000/conversation',
                {
                    message: inputText
                }
            )
                .then(res => {
                    setResponseText(res.data.response)
                })

        } else if (currentVocabWord.trim()) {
            axios.post('http://127.0.0.1:8000/answer',
                {
                    vocab: currentVocabWord,
                    guess: inputText
                }
            )
                .then(res => {
                    setIntent(res.data.intent)
                    setCurrentVocabWord('')
                    setResponseText(
                        res.data.response == "True" ?
                            "That's correct!" : "That is not correct."
                    )
                })

        } else {
            axios.post('http://127.0.0.1:8000/chat',
                {
                    message: inputText
                }
            )
                .then(res => {
                    console.log(res.data.intent)
                    setResponseText(res.data.response)
                    setIntent(res.data.intent)

                    if (res.data.vocab_word) {
                        setCurrentVocabWord(res.data.vocab_word)
                    }
                })

                .catch(err => {
                    console.log(err)
                })
        }
    }

    useEffect(() => {
        if (responseText.trim()) {

            const newServerMessage = {
                from: Sender.SERVER,
                message: responseText.trim()
            }

            setChatMessageList(prev => [...prev, newServerMessage])
            setResponseText('')
        }

    }, [responseText])

    return (

        <div
            className="text-display-container"
        >
            {chatMessageList.length > 0 ? (
                <div
                    className="chat-message-list"
                >
                    {chatMessageList.map((chatMessage, index) => (
                        <li
                            key={index}
                            className={chatMessage.from === Sender.USER ?
                                "user-message" : "bot-message"}
                        >
                            {chatMessage.message}
                        </li>
                    ))}

                    <div
                        ref={bottomRef}
                    />

                </div>

            ) : (

                <div
                    className="prompt-send"
                >
                    Send a message to start a conversation with the bot!
                </div>
            )}

            <div
                className="user-input-container"
            >
                <textarea
                    className="user-textbox"
                    rows={3}
                    value={inputText}
                    onChange={handleInput}
                    placeholder="Enter text here"
                />

                <button
                    className="user-submit-button"
                    onClick={handleSubmitButton}
                >
                    Send
                </button>
            </div>
        </div >
    )
}

export default TextDisplayComponent