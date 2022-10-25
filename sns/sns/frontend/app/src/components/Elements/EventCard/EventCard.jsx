import * as React from "react";
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

const CenterStyle = styled.div`
    font-family: arial;
    font-size: 24px;
    margin: 25px;
    width: 1350px;
    height: 200px;
`;

export const EventCard = () => {
    return (
        <CenterStyle>
            <ul>
                <li>
                    <Card sx={{ maxWidth: 345 }}>
                        <CardHeader
                            avatar={
                                <Avatar
                                    alt="Remy Sharp"
                                    src={`${process.env.PUBLIC_URL}/icon.png`}
                                />
                            }
                            action={
                                <IconButton aria-label="settings">
                                    <MoreVertIcon />
                                </IconButton>
                            }
                            title="nkoguchiDev"
                            subheader="Sep 14, 2016"
                        />
                        <CardContent>
                            <Typography variant="body2" color="text.secondary">
                                本文
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
                </li>
            </ul>
        </CenterStyle>
    );
};
