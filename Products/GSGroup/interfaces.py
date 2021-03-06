# -*- coding: utf-8 -*-
############################################################################
#
# Copyright IOPEN Technologies Ltd., 2003, Copyright © 2015 OnlineGroups.net
# and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
"""Interfaces for GroupServer Groups.

Most of the interfaces define the information relating to a particular
group activity. The are of the same rough form, with two main methods
  * Ability: Does the user have the ability to carry out a particular
    activity?
  * Status: Describe the user's ability to carry out a particular
    activity. It is assumed that a verb precedes the return value, and
    no return value ends in a full stop (alias period). For example
      "not a member", "an administrator", "insufficient cake"
    No Verbs Allowed!
The exceptions to this basic idiom are the administration interfaces, and
the "IGSModerationInfo", interface. The latter does not have any methods,
and supplies information about the entire group; the former also proides
methods for determining the type of administrator the user is.
"""
from __future__ import unicode_literals
from zope.interface import Interface
from zope.schema import Field, Text, Tuple, Bool
#from interfacesprivacy import *


class IGSGroupInfo(Interface):
    def group_exists(self):
        """True if the group folder exists"""
    def get_id(self):
        """Get the ID of the group"""
    def get_name(self):
        """Get the name of the group"""
    def get_url(self):
        """Get the URL of the group"""
    def get_property(self, prop, default):
        """Get a property of the group folder"""


class IGSMailingListInfo(Interface):
    def is_moderated(self):
        """True if the group is moderated, False otherwise"""
    def is_moderate_new(self):
        """True if new members are moderated, False otherwise"""
    def get_moderators(self):
        """Return the moderators as a list of userInfo objects."""
    def get_moderatees(self):
        """Return the moderatees as a list of userInfo objects."""
    def get_blocked_members(self):
        """Return the blocked members as a list of userInfo objects."""


# Joining


class IGSJoiningInfo(Interface):
    """Joining information for a group."""

    context = Field(
        title='Context',
        description='Group-context for the joining information')

    joinability = Text(
        title='Joinability',
        description='The joining-status for the group.',
        readonly=True)

    def can_join(user):
        """Can the user can join the group?

          ARGUMENTS
            "user" A user.

          RETURNS
            "True" if the user is not a group member and can join the group;
            "False" otherwise.

          SIDE EFFECTS
            None.
          """
    def status(user):
        """Can the user can leave the group?

        ARGUMENTS
          "user" A user.

        RETURNS
          A string stating whether the user is in the group, if the user
          can join the group, and how to join.

        SIDE EFFECTS
          None.
        """


class IGSLeavingInfo(Interface):
    """Leaving information for a group."""

    context = Field(
        title='Context',
        description='Group-context for the leaving information')

    leavability = Text(
        title='Leavability',
        description='The leaving-status for the group.',
        readonly=True)

    def can_leave(user):
        """Can the user can leave the group?

        ARGUMENTS
          "user" A user.

        RETURNS
          "True" if the user is a group member and can leave the group;
          "False" otherwise.

        SIDE EFFECTS
          None.
        """

    def status(user):
        """The leaving-status for a user

        ARGUMENTS
          "user": A user.

        RETURNS
          A string stating that the user can leave the group, or describing
          why the user cannot leave the group.

        SIDE EFFECTS
          None
        """

# Administration

# --=mpj17=-- Should the participation coach information be separated out?


class IGSSiteAdministrationInfo(Interface):
    """Site administration information"""

    context = Field(
        title='Context',
        description='Context for the site administration information')

    siteAdministrators = Tuple(
        title='Site Administrators',
        description='All the administrators for the site.',
        readonly=True)

    def site_administrator(user):
        """Whether the user a site administrator.

        ARGUMENTS
          "user": A user.

        RETURNS
          "True" if the user is a site administrator; "False" otherwise.

        SIDE EFFECTS
          None
        """


class IGSParticipationCoachInfo(Interface):
    """Participation Coach Information"""

    participationCoach = Field(
        title='Participation Coach',
        description='The participation coach for the group',
        readonly=True)

    def coach(user):
        """Is the user a participation coach?

        ARGUMENTS
          "user": A user.

        RETURNS
          "True" if the user is a participation coach; "False" otherwise.

        SIDE EFFECTS
          None
        """

    def status(user):
        """Paricipation coach status of the user

        ARGUMENTS
          "user": A user.

        RETURNS
          A string describing the participation-coach status of the user.

        SIDE EFFECTS
          None.
        """


class IGSGroupAdmistrationInfo(Interface):
    """Group administration information"""

    groupAdministrators = Tuple(
        title='Group Administrators',
        description='All users that have the group administrator role',
        readonly=True)

    def administrator(user):
        """Can the user administer the group?

        ARGUMENTS
          "user": A user.

        RETURNS
          "True" if the user is a site administrator, or a group
          administrator; "False" otherwise.

        SIDE EFFECTS
          None
        """

    def group_administrator(user):
        """Is the user a group administrator?

        ARGUMENTS
          "user": A user.

        RETURNS
          "True" if the user is a site administrator; "False" otherwise.

        SIDE EFFECTS
          None
        """

    def status(user):
        """Administration status of the user.

        ARGUMENTS
          "user": A user.

        RETURNS
          A string describing the administration status of the user.

        SIDE EFFECTS
          None."""

# Moderation


class IGSModerationInfo(Interface):
    """The moderation information for the group as a whole, rather than
    information about any particular user."""

    context = Field(
        title='Context',
        description='Context for the site moderation information')

    moderationOn = Bool(
        title='Moderation On',
        description='True if moderation on for the group',
        readonly=True)

    moderationStatus = Text(
        title='Moderation Status',
        description='The moderation status for the group',
        readonly=True)


class IGSModeratedInfo(Interface):
    """Information about the users who are moderated in the group"""

    context = Field(
        title='Context',
        description='Context for the moderated-user information')

    moderatedMembers = Tuple(
        title='Moderated Members',
        description='The moderated members in the group.')

    def moderated(user):
        """Is the user moderated?
        ARGUMENTS
          "user": A user.

        RETURNS
          "True" if posts from the user are moderated; "False" otherwise.

        SIDE EFFECTS
          None
        """

    def status(user):
        """The moderation status for the user in the group.

        ARGUMENTS
          "user": A user.

        RETURNS
          A string describing the moderation status of the user in the
          group.

        SIDE EFFECTS
          None
        """


class IGSModeratorInfo(Interface):
    """Information about the users who are moderators in the group"""

    context = Field(
        title='Context',
        description='Context for the moderator information')

    moderators = Tuple(
        title='Moderators',
        description='The members who are moderators in the group',
        readonly=True)

    def moderator(user):
        """Is the user a moderator?
        ARGUMENTS
          "user": A user.

        RETURNS
          "True" if the user is a moderator in the group; "False"
          otherwise.

        SIDE EFFECTS
          None
        """

    def status(user):
        """The moderator status for the user in the group.

        ARGUMENTS
          "user": A user.

        RETURNS
          A string describing the moderation status for the user in the
          group.

        SIDE EFFECTS
          None
        """

# Viewing


class IGSViewingInfo(Interface):
    """Information about viewing areas of a group.

    There are three areas that can have viewing privilages seperate to
    those specified for the entire group:
      * Messages,
      * Chat, and
      * The list of members.
    Information about the visibility of each of the areas, and the entire
    group, is provided by the methods defined here.
    """

    context = Field(
        title='Context',
        description='Context for the viewing information')

    whoCanView = Text(
        title='Who Can View the Area of the Group',
        description='A description of the users who can view the '
                    'particular area of the group',
        readonly=True)

    def can_view(user):
        """Can the user view the area?

        ARGUMENTS
          "user": A user.

        RETURNS
          "True" if the user can view the group and the area; "False"
          otherwise.

        SIDE EFFECTS
          None
        """

    def status(user):
        """The status of the user, with respect to viewing the area of the
        group.

        ARGUMENTS
          "user": A user.

        RETURNS
          A string describing the status of the user, with respect to
          viewing the area of the group.

        SIDE EFFECTS
          None
        """


class IGSGroupViewingInfo(IGSViewingInfo):
    """Information about who can view the group"""


class IGSMembersViewingInfo(IGSViewingInfo):
    """Group-Membership Viewing Information"""


class IGSMessageViewingInfo(IGSViewingInfo):
    """Information about who can view the posts that are added to the
    group."""


class IGSChatViewingInfo(IGSViewingInfo):
    """Information about who can view the chat-messages that are added to
    the group."""

# Posting


class IGSPostingInfo(Interface):
    """Information about posting to a group."""

    context = Field(
        title='Context',
        description='Context for the posting information')

    whoCanPost = Text(
        title='Who Can Post to the Group',
        description='A description of who can post messages to the group',
        readonly=True)

    def can_post(user):
        """Can the user post messages to the group?

        ARGUMENTS
          "user": A user.

        RETURNS
          "True" if the user can post messages and files to the
          group; "False" otherwise.

        SIDE EFFECTS
          None
        """

    def status(user):
        """The posting-status of the user.

        ARGUMENTS
          "user": A user.

        RETURNS
          A string describing the posting-status of the user.

        SIDE EFFECTS
          None
        """


class IGSMessagePostingInfo(IGSPostingInfo):
    """Information about posting messages to the group"""


class IGSChatPostingInfo(IGSPostingInfo):
    """Information about posting chat messages to the group"""
