from Utils.APIs.apis import get_tracklists
from Utils.DataStructures.ds import LinkedList, Node


def app():
    # Fetch the tracklist of relases
    releases = get_tracklists()
    current_rel, current_track = 'No release selected', Node(
        'No track selected')

    #Linked List to manage tracklist
    tracklist = LinkedList()

    # Menu options string
    main_menu = """

Main menu 
===================

1. Select Release
2. Next track
3. Previous track
4. Exit
Current Release: {}
Current Track: {}

Select an option: """

    while True:
        # Captures the menu selection
        selection = input(main_menu.format(current_rel, current_track.value))

        if selection == '1':
            # Build the releases menu
            rel_menu = lambda rel_list: ''.join([
                '{}- {} \n'.format(index,
                                   list(rel.keys())[0])
                for index, rel in zip(range(1,
                                            len(rel_list) + 1), rel_list)
            ])
            releases_menu = """

Releases Menu
=====================

{}

Select an option: """

            # Get the release selection
            selection = input(releases_menu.format(rel_menu(releases)))

            rel_dic = releases[int(selection) - 1]
            rel_name = list(rel_dic.keys())[0]
            rel_tracks = list(rel_dic.values())[0]

            # Set the tracks list to a Linked List
            tracklist = LinkedList(l=rel_tracks)
            # Set the values for the current release,
            # and the current track as the head of the Linked List
            current_rel, current_track = rel_name, tracklist.head

        # Set the current track to the next node
        if selection == '2':
            if current_track.next:
                current_track = current_track.next

        # Traverse the list until the current next node is the actual tack node
        if selection == '3':
            for track in tracklist:
                if track.next == current_track:
                    current_track = track

        # Exits the app
        if selection == '4':
            break
