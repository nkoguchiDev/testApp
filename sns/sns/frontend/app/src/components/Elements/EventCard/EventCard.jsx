import * as React from "react";
import { useEffect } from "react";
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

const CardList = styled.li`
    display: block;
`;

export const EventCard = (props) => {
    useEffect(() => {
        return () => {
            setMessagesToCards(props.user, props.events);
        };
    });

    const setMessagesToCards = (user, events) => {
        getMessageList().then(
            (result) => {
                const element = document.getElementById("events");
                for (let e in events) {
                    const card = (
                        <CardList>
                            <Card sx={{ maxWidth: 345 }}>
                                <CardHeader
                                    avatar={
                                        <Avatar
                                            alt="message post user name"
                                            src={`${process.env.PUBLIC_URL}/icon.png`}
                                        />
                                    }
                                    action={
                                        <IconButton aria-label="settings">
                                            <MoreVertIcon />
                                        </IconButton>
                                    }
                                    title="message post user name"
                                    // subheader={e.created}
                                    subheader="date"
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
                                        <IconButton>
                                            <DeleteIcon />
                                        </IconButton>
                                    </Tooltip>
                                </CardActions>
                            </Card>
                        </CardList>
                    );
                    element.appendChild(card);
                }
            },
            (error) => alert("error")
        );
    };

    return (
        <center>
            <ul id="events" />
        </center>
    );
};
