import * as React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

import styled from "styled-components";

import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Avatar from "@mui/material/Avatar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import FavoriteIcon from "@mui/icons-material/Favorite";
import ShareIcon from "@mui/icons-material/Share";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import DeleteIcon from "@mui/icons-material/Delete";
import Tooltip from "@mui/material/Tooltip";

import { getMessageList } from "./../../../features/messages/api/getMessageList";
import { deleteMessage } from "../../../features/api/messages";

const CardList = styled.li`
    display: block;
    margin: 5px;
`;

export const EventCard = () => {
    const navigate = useNavigate();
    const [events, setEvents] = React.useState([]);

    useEffect(() => {
        return () => {
            setMessagesToCards();
        };
    }, []);

    const setMessagesToCards = () => {
        return getMessageList().then(
            (result) => setEvents(result),
            (error) => navigate("/forbidden")
        );
    };
    const deleteEventCard = (id) => {
        deleteMessage(id);

        window.location.reload();
    };
    return (
        <div>
            <ul id="events">
                {events.map((e, i) => (
                    <CardList id={i} key={i}>
                        <Card variant="outlined" sx={{ maxWidth: 350, margin: "auto" }}>
                            <CardHeader
                                avatar={
                                    <Avatar
                                        alt={e.create_user}
                                        src={`${process.env.PUBLIC_URL}/icon.png`}
                                    />
                                }
                                action={
                                    <IconButton aria-label="settings">
                                        <MoreVertIcon />
                                    </IconButton>
                                }
                                title={e.create_user}
                                subheader={e.date}
                            />
                            <CardContent>
                                <Typography variant="body2" color="text.secondary">
                                    {e.content}
                                </Typography>
                            </CardContent>
                            <CardActions disableSpacing>
                                <IconButton aria-label="add to favorites">
                                    <FavoriteIcon />
                                </IconButton>
                                <IconButton aria-label="share">
                                    <ShareIcon />
                                </IconButton>
                                <Tooltip title="Delete">
                                    <IconButton
                                        onClick={deleteEventCard.bind(this, e.uuid)}
                                    >
                                        <DeleteIcon />
                                    </IconButton>
                                </Tooltip>
                            </CardActions>
                        </Card>
                    </CardList>
                ))}
            </ul>
        </div>
    );
};
