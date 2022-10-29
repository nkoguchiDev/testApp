import { axios } from "/app/src/lib/axios";

export const createMessage = (content) => {
    return axios.post(
        "/messages",
        { content },
        {
            headers: {
                "Content-Type": "application/json",
            },
            withCredentials: true,
        }
    );
};

export const getMessageList = () => {
    return axios.get("/messages", {
        withCredentials: true,
    });
};

export const deleteMessage = (id) => {
    return axios.delete(`/messages/${id}`, {
        withCredentials: true,
    });
};
