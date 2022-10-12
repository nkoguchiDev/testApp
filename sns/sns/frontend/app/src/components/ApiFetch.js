import React, {useState, useEffect} from 'react'
import axios from 'axios'

const ApiFetch = () => {

    const [posts, setPosts] = useState([])

    useEffect(() => {
        axios.get('http://localhost/message')
        .then(res => {
            setPosts(res.data)
        })
    },[])

    return (
        <div>
            <h1>{posts.msg}</h1>
        </div>
    )
}

export default ApiFetch