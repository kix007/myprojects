using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneLoader : MonoBehaviour
{
    private int indexId;
    private string levelToLoadName = "";
    public List<string> levelNames = new List<string>();

    // Only using start as an example.
    public void NextLevel()
    {
        // If you run into any problems with this. Try putting either -1 or levelNames.Count - 1;
        indexId = Random.Range(0, levelNames.Count - 1);
        //Debug.Log(indexId);
        // We now set the levelToLoadName to the name of the string at the index inside the List.
        levelToLoadName = levelNames[indexId];
        SceneManager.LoadScene(levelToLoadName);        // Now we load the level.

    }
}
